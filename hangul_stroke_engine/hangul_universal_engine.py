"""
Hangul Universal Stroke Engine (Noto Sans CJK KR) - Master Jamo Modular Edition
================================================================================
Automated stroke-order extraction, decomposition, and mathematical verification
for all Korean Hangul syllables (KS X 1001 2,350 and Unicode 11,172)
powered by the 258 Canonical Master Jamo Modular Library.
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

FONT_PATH = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
MASTER_DB_PATH = '/home/antigravity/parkjinsoo8485/machine_learning/hangul_stroke_engine/master_jamo_library.json'
CALIBRATED_DB_PATH = '/home/antigravity/parkjinsoo8485/machine_learning/hangul_stroke_engine/calibrated_strokes_db.json'

CHO_LIST = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
JUNG_LIST = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
JONG_LIST = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

VERTICAL_VOWELS = set(['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅣ'])
HORIZONTAL_VOWELS = set(['ㅗ','ㅛ','ㅜ','ㅠ','ㅡ'])
COMPOUND_VOWELS = set(['ㅘ','ㅙ','ㅚ','ㅝ','ㅞ','ㅟ','ㅢ'])

class HangulUniversalEngine:
    def __init__(self, font_path: str = FONT_PATH, master_db_path: str = MASTER_DB_PATH):
        self.font = TTFont(font_path, fontNumber=2)
        self.glyph_set = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()

        # Load Master Jamo Modular Library
        if os.path.exists(master_db_path):
            with open(master_db_path, 'r', encoding='utf-8') as f:
                self.master_lib = json.load(f)
        else:
            self.master_lib = None

        # Load Calibrated Syllables DB (Anchor Truths)
        if os.path.exists(CALIBRATED_DB_PATH):
            with open(CALIBRATED_DB_PATH, 'r', encoding='utf-8') as f:
                self.calibrated_db = json.load(f)
        else:
            self.calibrated_db = {}

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
            arch = 'M2' if has_jong else 'M1'
            
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
        """Generates full stroke list with clipping masks and trajectories from Master Jamo Library."""
        # 1. Fast-path: check if character has a verified handcrafted anchor calibration
        if syllable in self.calibrated_db:
            val = self.calibrated_db[syllable]
            strokes = val['strokes'] if isinstance(val, dict) and 'strokes' in val else val
            return copy_strokes(strokes)

        info = self.decompose(syllable)
        cho, jung, jong, arch = info['cho'], info['jung'], info['jong'], info['archetype']
        strokes = []
        curr_order = 1

        if not self.master_lib:
            raise RuntimeError("Master Jamo Library is not loaded.")

        # 1. Cho Component (1 of 114)
        cho_entry = self.master_lib['cho_modules'].get(cho, {}).get(arch)
        if cho_entry:
            for s in cho_entry['strokes']:
                st = dict(s)
                st['order'] = curr_order
                strokes.append(st)
                curr_order += 1

        # 2. Jung Component (1 of 63)
        # Select beol based on syllable layout:
        # beol_1: V1, H1, M1 (무받침)
        # beol_2: V2, H2, M2 (단순받침)
        # beol_3: complex / double adjustments
        if not info['has_jong']:
            beol_key = 'beol_1'
        else:
            beol_key = 'beol_2'

        jung_entry = self.master_lib['jung_modules'].get(jung, {}).get(beol_key)
        if jung_entry:
            for s in jung_entry['strokes']:
                st = dict(s)
                st['order'] = curr_order
                strokes.append(st)
                curr_order += 1

        # 3. Jong Component (1 of 81)
        if info['has_jong']:
            jong_layout = 'V2' if arch in ('V1', 'V2') else ('H2' if arch in ('H1', 'H2') else 'M2')
            jong_entry = self.master_lib['jong_modules'].get(jong, {}).get(jong_layout)
            if jong_entry:
                for s in jong_entry['strokes']:
                    st = dict(s)
                    st['order'] = curr_order
                    strokes.append(st)
                    curr_order += 1

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

def copy_strokes(strokes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    import copy
    return copy.deepcopy(strokes)

if __name__ == '__main__':
    engine = HangulUniversalEngine()
    print("Testing Universal Engine with Master Jamo Library across all 6 archetypes...")
    samples = ['가', '각', '고', '곡', '과', '광', '별', '한', '글', '꽃', '꿈', '물', '봄', '귀', '황', '권', '꿩']
    for s in samples:
        data = engine.process_syllable(s, verify=True)
        v = data['verification']
        print(f"[{s}] {data['decomposition']:13s} | Layout: {data['archetype']:2s} | Strokes: {data['total_strokes']:2d} | Coverage: {v['coverage_pct']:7.4f}% (Unfilled: {v['unfilled_pixels']:5d} px, Leakage: {v['leakage_pixels']:2d} px)")
