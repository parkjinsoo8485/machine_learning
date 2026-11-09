"""
Contour Auto-Aligner for Hangul Stroke Engine (Stage 1)
=======================================================
Inspects OpenType CFF font contours directly from Noto Sans CJK KR
to extract precise bounding boxes, centerlines, and clip bounds
for Cho, Jung, and Jong components of any Hangul syllable.
"""

from typing import Dict, List, Tuple, Any, Optional
import numpy as np
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen

FONT_PATH = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'

CHO_LIST = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
JUNG_LIST = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
JONG_LIST = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

VERTICAL_VOWELS = set(['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅣ'])
HORIZONTAL_VOWELS = set(['ㅗ','ㅛ','ㅜ','ㅠ','ㅡ'])

class ContourAligner:
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

    def get_contours(self, syllable: str) -> List[Dict[str, Any]]:
        gid = self.cmap[ord(syllable)]
        rp = RecordingPen()
        self.glyph_set[gid].draw(rp)
        contours, curr = [], []
        for op, args in rp.value:
            if op == 'moveTo':
                if curr: contours.append(curr)
                curr = [args[0]]
            elif op in ('lineTo', 'curveTo', 'qCurveTo'):
                for a in args:
                    if isinstance(a, tuple): curr.append(a)
            elif op in ('closePath', 'endPath'):
                if curr: contours.append(curr)
                curr = []
        if curr: contours.append(curr)

        res = []
        for c in contours:
            pts = np.array([(p[0], 880 - p[1]) for p in c])
            res.append({
                'min_x': float(pts[:, 0].min()), 'max_x': float(pts[:, 0].max()),
                'min_y': float(pts[:, 1].min()), 'max_y': float(pts[:, 1].max()),
                'cx': float((pts[:, 0].min() + pts[:, 0].max()) / 2),
                'cy': float((pts[:, 1].min() + pts[:, 1].max()) / 2),
                'w': float(pts[:, 0].max() - pts[:, 0].min()),
                'h': float(pts[:, 1].max() - pts[:, 1].min()),
                'pts': pts
            })
        return res

    def extract_jamo_bounds(self, syllable: str) -> Dict[str, Dict[str, float]]:
        info = self.decompose(syllable)
        arch = info['archetype']
        contours = self.get_contours(syllable)
        if not contours:
            return {}

        cho_c, jung_c, jong_c = [], [], []

        if arch == 'V1':
            for c in contours:
                if c['cx'] < 560 and c['min_x'] < 520:
                    cho_c.append(c)
                else:
                    jung_c.append(c)
        elif arch == 'V2':
            for c in contours:
                if c['min_y'] > 540 and c['max_y'] > 850:
                    jong_c.append(c)
                elif c['min_x'] > 520 and c['h'] > 350:
                    jung_c.append(c)
                else:
                    cho_c.append(c)
        elif arch == 'H1':
            for c in contours:
                if c['cy'] < 480 and c['min_y'] < 400:
                    cho_c.append(c)
                else:
                    jung_c.append(c)
        elif arch == 'H2':
            for c in contours:
                if c['min_y'] > 540 and c['max_y'] > 850:
                    jong_c.append(c)
                elif c['w'] > 750:
                    jung_c.append(c)
                elif c['min_y'] < 430:
                    cho_c.append(c)
                else:
                    jung_c.append(c)
        else: # C1, C2
            for c in contours:
                if info['has_jong'] and c['min_y'] > 580 and c['max_y'] > 850:
                    jong_c.append(c)
                elif c['min_x'] > 600 and c['h'] > 350:
                    jung_c.append(c)
                elif c['min_x'] < 500 and c['min_y'] < 430:
                    cho_c.append(c)
                else:
                    jung_c.append(c)

        def merge_bounds(c_list):
            if not c_list: return None
            return {
                'x0': min(c['min_x'] for c in c_list),
                'x1': max(c['max_x'] for c in c_list),
                'y0': min(c['min_y'] for c in c_list),
                'y1': max(c['max_y'] for c in c_list),
                'cx': (min(c['min_x'] for c in c_list) + max(c['max_x'] for c in c_list)) / 2,
                'cy': (min(c['min_y'] for c in c_list) + max(c['max_y'] for c in c_list)) / 2,
                'w': max(c['max_x'] for c in c_list) - min(c['min_x'] for c in c_list),
                'h': max(c['max_y'] for c in c_list) - min(c['min_y'] for c in c_list)
            }

        return {
            'cho': merge_bounds(cho_c),
            'jung': merge_bounds(jung_c),
            'jong': merge_bounds(jong_c)
        }
