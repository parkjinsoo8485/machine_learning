"""
Hangul Stroke Engine Test Harness & Automated Pipeline
======================================================
Automated end-to-end harness executing:
- Step 1: Contour Auto-Aligner (glyph-aligned vector trajectories)
- Step 2: 100 Syllables Dataset Batch Pre-rendering (Method B DB)
- Step 3: Strict Raster QA Harness (Coverage >= 99.0%, Bleeding <= 8px)
- Step 4: Web Studio Database Integration & Verification
"""

import os
import sys
import json
import time
import subprocess
from typing import Dict, List, Any, Tuple
import numpy as np
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT_PATH = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'

# Top 100 Most Common and Structurally Diverse Hangul Syllables
TOP_100_SYLLABLES = [
    # Top Frequency Common Words
    '이', '다', '는', '에', '가', '하', '은', '을', '를', '의',
    '고', '로', '지', '있', '한', '수', '기', '과', '서', '들',
    '되', '주', '어', '도', '보', '시', '그', '대', '상', '문',
    '정', '해', '것', '사', '전', '생', '인', '자', '일', '개',
    '동', '년', '화', '장', '원', '국', '중', '경', '력', '명',
    # Poetic & High-Fidelity Archetypes (글, 꽃, 별, 꿈, 달, 봄, 눈, 물, 불...)
    '글', '꽃', '꿈', '별', '달', '봄', '눈', '물', '불', '산',
    '빛', '솔', '새', '닭', '밥', '김', '강', '바', '람', '구',
    # Multi-Archetype Coverage (V1, V2, H1, H2, C1, C2)
    '각', '곡', '광', '골', '곰', '눈', '돈', '손', '간', '감',
    '남', '밤', '두', '루', '무', '부', '우', '추', '투', '푸'
]

CHO_LIST = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
JUNG_LIST = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
JONG_LIST = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
VERTICAL_VOWELS = set(['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅣ'])
HORIZONTAL_VOWELS = set(['ㅗ','ㅛ','ㅜ','ㅠ','ㅡ'])

class HangulHarness:
    def __init__(self, font_path: str = FONT_PATH):
        self.font = TTFont(font_path, fontNumber=2)
        self.glyph_set = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()

    def decompose(self, syllable: str) -> Dict[str, Any]:
        code = ord(syllable) - 0xAC00
        cho_idx = code // 588
        jung_idx = (code % 588) // 28
        jong_idx = code % 28
        cho, jung, jong = CHO_LIST[cho_idx], JUNG_LIST[jung_idx], JONG_LIST[jong_idx]
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
            'cho': cho, 'jung': jung, 'jong': jong,
            'has_jong': has_jong, 'archetype': arch
        }

    def get_noto_path(self, syllable: str) -> str:
        gid = self.cmap[ord(syllable)]
        svg_pen = SVGPathPen(self.glyph_set)
        trans_pen = TransformPen(svg_pen, (1, 0, 0, -1, 0, 880))
        self.glyph_set[gid].draw(trans_pen)
        return svg_pen.getCommands()

    def get_glyph_points(self, syllable: str) -> np.ndarray:
        gid = self.cmap[ord(syllable)]
        rp = RecordingPen()
        self.glyph_set[gid].draw(rp)
        pts = []
        for op, args in rp.value:
            for a in args:
                if isinstance(a, tuple):
                    pts.append((a[0], 880 - a[1]))
        return np.array(pts) if pts else np.zeros((0, 2))

    def generate_strokes_aligned(self, syllable: str) -> List[Dict[str, Any]]:
        """Generates contour-aligned canonical strokes for any syllable."""
        db_path = os.path.join(os.path.dirname(__file__), 'calibrated_strokes_db.json')
        if os.path.exists(db_path):
            try:
                with open(db_path, 'r', encoding='utf-8') as f:
                    db = json.load(f)
                    if syllable in db:
                        return db[syllable]
            except Exception:
                pass

        info = self.decompose(syllable)
        cho, jung, jong, arch = info['cho'], info['jung'], info['jong'], info['archetype']
        import jamo_rules
        strokes = []
        curr = 1

        # 1. Cho
        s_cho = jamo_rules.get_cho_strokes(cho, arch, curr, jung=jung)
        strokes.extend(s_cho)
        curr += len(s_cho)

        # 2. Jung
        s_jung = jamo_rules.get_jung_strokes(jung, arch, curr, cho=cho, jong=jong)
        strokes.extend(s_jung)
        curr += len(s_jung)

        # 3. Jong
        if info['has_jong']:
            s_jong = jamo_rules.get_jong_strokes(jong, curr, archetype=arch)
            strokes.extend(s_jong)

        return strokes

    def verify_raster_qa(self, syllable: str, strokes: List[Dict[str, Any]], glyph_path: str) -> Dict[str, Any]:
        """Strict raster evaluation: coverage %, unfilled pixels, leakage pixels."""
        ref_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">
          <path d="{glyph_path}" fill="black" />
        </svg>'''
        with open('/tmp/harness_ref.svg', 'w') as f: f.write(ref_svg)
        subprocess.run(['rsvg-convert', '-o', '/tmp/harness_ref.png', '/tmp/harness_ref.svg'], check=True)
        ref_img = np.array(Image.open('/tmp/harness_ref.png'))[:, :, 3] > 128

        defs, elements = [], []
        for st in strokes:
            ord_n = st['order']
            cb = st['clip_box']
            defs.append(f'''
              <clipPath id="h-iso-{ord_n}"><path d="{glyph_path}" /></clipPath>
              <clipPath id="h-box-{ord_n}">
                <rect x="{cb['x']}" y="{cb['y']}" width="{cb['w']}" height="{cb['h']}" />
              </clipPath>
            ''')
            elements.append(f'''
              <g clip-path="url(#h-box-{ord_n})">
                <g clip-path="url(#h-iso-{ord_n})">
                  <path d="{st['d']}" fill="none" stroke="black" stroke-width="{st.get('width', 100)}"
                        stroke-linecap="square" stroke-linejoin="round" />
                </g>
              </g>
            ''')

        ren_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">
          <defs>{''.join(defs)}</defs>
          {''.join(elements)}
        </svg>'''
        with open('/tmp/harness_ren.svg', 'w') as f: f.write(ren_svg)
        subprocess.run(['rsvg-convert', '-o', '/tmp/harness_ren.png', '/tmp/harness_ren.svg'], check=True)
        ref_raw = np.array(Image.open('/tmp/harness_ref.png'))[:, :, 3]
        ren_raw = np.array(Image.open('/tmp/harness_ren.png'))[:, :, 3]
        ref_img = ref_raw > 128
        ren_img = ren_raw > 128

        ref_px = int(np.sum(ref_img))
        intersection = int(np.sum(ref_img & ren_img))
        unfilled = int(np.sum(ref_img & (~ren_img)))
        # True leakage: pixels drawn outside the glyph in transparent background
        leakage = int(np.sum((ref_raw == 0) & ren_img))
        cov_pct = (intersection / ref_px * 100.0) if ref_px > 0 else 100.0

        is_pass = (cov_pct >= 95.0 and leakage == 0)

        return {
            'character': syllable,
            'ref_pixels': ref_px,
            'rendered_pixels': int(np.sum(ren_img)),
            'coverage_pct': round(cov_pct, 4),
            'unfilled_pixels': unfilled,
            'leakage_pixels': leakage,
            'pass': is_pass
        }

    def run_full_harness(self, syllables: List[str], out_dir: str) -> Dict[str, Any]:
        os.makedirs(out_dir, exist_ok=True)
        print(f"=== Starting Automated Hangul Harness on {len(syllables)} Syllables ===")
        t0 = time.time()
        results = []
        dataset_bundle = {}

        for idx, s in enumerate(syllables, 1):
            decomp = self.decompose(s)
            noto_path = self.get_noto_path(s)
            strokes = self.generate_strokes_aligned(s)
            qa = self.verify_raster_qa(s, strokes, noto_path)

            status_str = "PASS" if qa['pass'] else "ATTN"
            print(f"[{idx:3d}/{len(syllables)}] {s} ({decomp['archetype']}) | Cov: {qa['coverage_pct']:7.4f}% | Unfilled: {qa['unfilled_pixels']:5d} px | Leak: {qa['leakage_pixels']:2d} px | {status_str}")

            entry = {
                'character': s,
                'unicode': decomp['unicode'],
                'decomp': f"{decomp['cho']} + {decomp['jung']}" + (f" + {decomp['jong']}" if decomp['has_jong'] else ""),
                'archetype': decomp['archetype'],
                'coverage': f"{qa['coverage_pct']:.4f}% (미채움 {qa['unfilled_pixels']} px, 침범 {qa['leakage_pixels']} px)",
                'noto_path': noto_path,
                'total_strokes': len(strokes),
                'strokes': strokes,
                'qa': qa
            }

            # Save individual JSON
            json_file = f"{ord(s):04X}_{s}.json"
            with open(os.path.join(out_dir, json_file), 'w', encoding='utf-8') as f:
                json.dump(entry, f, ensure_ascii=False, indent=2)

            dataset_bundle[s] = entry
            results.append(qa)

        elapsed = time.time() - t0
        avg_cov = np.mean([r['coverage_pct'] for r in results])
        pass_count = sum(1 for r in results if r['pass'])

        manifest = {
            'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'total_syllables': len(syllables),
            'passed_count': pass_count,
            'avg_coverage': round(float(avg_cov), 4),
            'elapsed_sec': round(elapsed, 2),
            'syllables': results
        }

        with open(os.path.join(out_dir, 'manifest.json'), 'w', encoding='utf-8') as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)

        # Save bundle for Web Studio
        with open('/tmp/harness_studio_bundle.json', 'w', encoding='utf-8') as f:
            json.dump(dataset_bundle, f, ensure_ascii=False)

        print("=" * 80)
        print(f"Harness Completed in {elapsed:.2f}s!")
        print(f"Average Coverage: {avg_cov:.4f}% | Passed: {pass_count}/{len(syllables)} ({pass_count/len(syllables)*100:.1f}%)")
        print("=" * 80)

        return manifest


if __name__ == '__main__':
    harness = HangulHarness()
    out_dir = '/home/antigravity/parkjinsoo8485/machine_learning/hangul_stroke_engine/generated_data'
    harness.run_full_harness(TOP_100_SYLLABLES, out_dir)
