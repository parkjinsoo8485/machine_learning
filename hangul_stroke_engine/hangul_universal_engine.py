"""
Hangul Universal Stroke Engine (Noto Sans CJK KR)
=================================================
Automated stroke-order extraction, decomposition, and mathematical verification
for all Korean Hangul syllables (KS X 1001 2,350 and Unicode 11,172).
"""

import os
import json
import subprocess
from typing import Dict, List, Tuple, Any, Optional
import numpy as np
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

import jamo_rules

FONT_PATH = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'

CHO_LIST = jamo_rules.CHO_LIST
JUNG_LIST = jamo_rules.JUNG_LIST
JONG_LIST = jamo_rules.JONG_LIST

VERTICAL_VOWELS = set(['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅣ'])
HORIZONTAL_VOWELS = set(['ㅗ','ㅛ','ㅜ','ㅠ','ㅡ'])
COMPOUND_VOWELS = set(['ㅘ','ㅙ','ㅚ','ㅝ','ㅞ','ㅟ','ㅢ'])

class HangulUniversalEngine:
    def __init__(self, font_path: str = FONT_PATH):
        self.font = TTFont(font_path, fontNumber=2)
        self.glyph_set = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()

    def decompose(self, syllable: str) -> Dict[str, Any]:
        """Decomposes any Hangul syllable into Cho, Jung, Jong and identifies layout archetype."""
        code = ord(syllable) - 0xAC00
        if not (0 <= code < 11172):
            raise ValueError(f"'{syllable}' is outside the Hangul Syllables block (U+AC00 ~ U+D7A3).")
        
        jong_idx = code % 28
        code //= 28
        jung_idx = code % 21
        cho_idx = code // 21
        
        cho = CHO_LIST[cho_idx]
        jung = JUNG_LIST[jung_idx]
        jong = JONG_LIST[jong_idx]
        
        has_jong = (jong != '')
        if jung in VERTICAL_VOWELS:
            arch = 'V2' if has_jong else 'V1'
        elif jung in HORIZONTAL_VOWELS:
            arch = 'H2' if has_jong else 'H1'
        else:
            arch = 'C2' if has_jong else 'C1'
            
        return {
            'character': syllable,
            'unicode': f'U+{ord(syllable):04X}',
            'cho': cho,
            'jung': jung,
            'jong': jong,
            'has_jong': has_jong,
            'archetype': arch
        }

    def get_noto_glyph_path(self, syllable: str) -> str:
        """Extracts exact SVG path for Noto Sans CJK KR (1000x1000 viewBox, Y-flipped)."""
        gid = self.cmap[ord(syllable)]
        svg_pen = SVGPathPen(self.glyph_set)
        trans_pen = TransformPen(svg_pen, (1, 0, 0, -1, 0, 880))
        self.glyph_set[gid].draw(trans_pen)
        return svg_pen.getCommands()

    def generate_strokes(self, syllable: str) -> List[Dict[str, Any]]:
        """Generates full stroke list with clipping masks and trajectories for any Hangul syllable."""
        info = self.decompose(syllable)
        cho, jung, jong, arch = info['cho'], info['jung'], info['jong'], info['archetype']
        strokes = []
        curr_order = 1

        # 1. Cho strokes
        s_cho = jamo_rules.get_cho_strokes(cho, arch, curr_order)
        strokes.extend(s_cho)
        curr_order += len(s_cho)

        # 2. Jung strokes
        s_jung = jamo_rules.get_jung_strokes(jung, arch, curr_order, cho=cho)
        strokes.extend(s_jung)
        curr_order += len(s_jung)

        # 3. Jong strokes
        if info['has_jong']:
            s_jong = jamo_rules.get_jong_strokes(jong, curr_order, archetype=arch)
            strokes.extend(s_jong)

        return strokes

    def verify_coverage(self, syllable: str, strokes: List[Dict[str, Any]],
                        glyph_path: str) -> Dict[str, Any]:
        """Renders SVG to raster and computes exact pixel coverage, unfilled count, and leakage."""
        ref_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">
          <path d="{glyph_path}" fill="black" />
        </svg>'''
        with open('/tmp/eng_ref.svg', 'w') as f: f.write(ref_svg)
        subprocess.run(['rsvg-convert', '-o', '/tmp/eng_ref.png', '/tmp/eng_ref.svg'], check=True)
        ref_img = np.array(Image.open('/tmp/eng_ref.png'))[:, :, 3] > 128

        # Render combined strokes
        defs, elements = [], []
        for st in strokes:
            order = st['order']
            cb = st['clip_box']
            defs.append(f'''
              <clipPath id="eng-iso-{order}"><path d="{glyph_path}" /></clipPath>
              <clipPath id="eng-box-{order}">
                <rect x="{cb['x']}" y="{cb['y']}" width="{cb['w']}" height="{cb['h']}" />
              </clipPath>
            ''')
            elements.append(f'''
              <g clip-path="url(#eng-box-{order})">
                <g clip-path="url(#eng-iso-{order})">
                  <path d="{st['d']}" fill="none" stroke="black" stroke-width="{st.get('width', 100)}"
                        stroke-linecap="square" stroke-linejoin="round" />
                </g>
              </g>
            ''')

        ren_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">
          <defs>{''.join(defs)}</defs>
          {''.join(elements)}
        </svg>'''
        with open('/tmp/eng_ren.svg', 'w') as f: f.write(ren_svg)
        subprocess.run(['rsvg-convert', '-o', '/tmp/eng_ren.png', '/tmp/eng_ren.svg'], check=True)
        ren_img = np.array(Image.open('/tmp/eng_ren.png'))[:, :, 3] > 128

        ref_pixels = int(np.sum(ref_img))
        intersection = int(np.sum(ref_img & ren_img))
        unfilled = int(np.sum(ref_img & (~ren_img)))
        leakage = int(np.sum((~ref_img) & ren_img))
        cov_pct = (intersection / ref_pixels) * 100.0 if ref_pixels > 0 else 100.0

        return {
            'character': syllable,
            'ref_pixels': ref_pixels,
            'coverage_pct': round(cov_pct, 4),
            'unfilled_pixels': unfilled,
            'leakage_pixels': leakage,
            'perfect': (unfilled == 0 and leakage == 0)
        }

    def process_syllable(self, syllable: str, verify: bool = True) -> Dict[str, Any]:
        """Complete pipeline: decomposes, extracts path, generates strokes, and optionally verifies."""
        info = self.decompose(syllable)
        glyph_path = self.get_noto_glyph_path(syllable)
        strokes = self.generate_strokes(syllable)

        res = {
            'character': syllable,
            'unicode': info['unicode'],
            'font': 'Noto Sans CJK KR Regular',
            'decomposition': f"{info['cho']} + {info['jung']}{(' + ' + info['jong']) if info['has_jong'] else ''}",
            'archetype': info['archetype'],
            'noto_glyph_path': glyph_path,
            'total_strokes': len(strokes),
            'strokes': strokes
        }

        if verify:
            metrics = self.verify_coverage(syllable, strokes, glyph_path)
            res['verification'] = metrics

        return res

if __name__ == '__main__':
    engine = HangulUniversalEngine()
    print("Testing Universal Engine on benchmark syllables...")
    samples = ['가', '각', '고', '곡', '과', '광', '별', '한', '글', '꽃', '꿈']
    for s in samples:
        data = engine.process_syllable(s, verify=True)
        v = data['verification']
        print(f"[{s}] {data['decomposition']:13s} | Archetype: {data['archetype']:2s} | Strokes: {data['total_strokes']:2d} | Coverage: {v['coverage_pct']:7.4f}% (Unfilled: {v['unfilled_pixels']:5d} px, Leakage: {v['leakage_pixels']:2d} px)")
