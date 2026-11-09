"""
Hangul Stroke Order Automated Generation & Verification Engine
=============================================================
This engine automates the generation of stroke-order SVG paths,
centerline medians, and stroke sequence metadata for Hangul syllables.
"""

import json
import os
from typing import Dict, List, Tuple, Any

# Unicode base offsets for Hangul
HANGUL_BASE = 0xAC00
CHOSUNG_LIST = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]
JUNGSUNG_LIST = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
]
JONGSUNG_LIST = [
    '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ',
    'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

# Classification of vowels into layout categories
# V: Vertical (ㅏ, ㅐ, ㅑ, ㅒ, ㅓ, ㅔ, ㅕ, ㅖ, ㅣ)
# H: Horizontal (ㅗ, ㅛ, ㅜ, ㅠ, ㅡ)
# VH: Mixed (ㅘ, ㅙ, ㅚ, ㅝ, ㅞ, ㅟ, ㅢ)
VOWEL_TYPE = {
    'ㅏ': 'V', 'ㅐ': 'V', 'ㅑ': 'V', 'ㅒ': 'V', 'ㅓ': 'V',
    'ㅔ': 'V', 'ㅕ': 'V', 'ㅖ': 'V', 'ㅣ': 'V',
    'ㅗ': 'H', 'ㅛ': 'H', 'ㅜ': 'H', 'ㅠ': 'H', 'ㅡ': 'H',
    'ㅘ': 'VH', 'ㅙ': 'VH', 'ㅚ': 'VH', 'ㅝ': 'VH', 'ㅞ': 'VH', 'ㅟ': 'VH', 'ㅢ': 'VH'
}

# Standard stroke templates for canonical Jamo in 0..100 coordinate space
# Each stroke has: 'name', 'points' [(x, y)...] (median line), 'path' (SVG path outline or stroke), 'type'
JAMO_STROKE_TEMPLATES: Dict[str, List[Dict[str, Any]]] = {
    # Consonants
    'ㄱ': [
        {'name': 'ㄱ (가로-세로 꺾음)', 'type': 'corner', 'points': [[15, 20], [80, 20], [80, 85]]}
    ],
    'ㄲ': [
        {'name': '첫째 ㄱ', 'type': 'corner', 'points': [[10, 20], [45, 20], [45, 85]]},
        {'name': '둘째 ㄱ', 'type': 'corner', 'points': [[55, 20], [90, 20], [90, 85]]}
    ],
    'ㄴ': [
        {'name': 'ㄴ (세로-가로 꺾음)', 'type': 'corner', 'points': [[20, 15], [20, 80], [85, 80]]}
    ],
    'ㄷ': [
        {'name': 'ㄷ 1획 (위 가로)', 'type': 'line', 'points': [[20, 20], [80, 20]]},
        {'name': 'ㄷ 2획 (ㄴ형태)', 'type': 'corner', 'points': [[20, 20], [20, 80], [80, 80]]}
    ],
    'ㄸ': [
        {'name': '첫 ㄷ 1획', 'type': 'line', 'points': [[10, 20], [45, 20]]},
        {'name': '첫 ㄷ 2획', 'type': 'corner', 'points': [[10, 20], [10, 80], [45, 80]]},
        {'name': '둘째 ㄷ 1획', 'type': 'line', 'points': [[55, 20], [90, 20]]},
        {'name': '둘째 ㄷ 2획', 'type': 'corner', 'points': [[55, 20], [55, 80], [90, 80]]}
    ],
    'ㄹ': [
        {'name': 'ㄹ 1획 (ㄱ형태)', 'type': 'corner', 'points': [[20, 20], [80, 20], [80, 50]]},
        {'name': 'ㄹ 2획 (가운데 가로)', 'type': 'line', 'points': [[20, 50], [80, 50]]},
        {'name': 'ㄹ 3획 (ㄴ형태)', 'type': 'corner', 'points': [[20, 50], [20, 80], [80, 80]]}
    ],
    'ㅁ': [
        {'name': 'ㅁ 1획 (좌측 세로)', 'type': 'line', 'points': [[20, 20], [20, 80]]},
        {'name': 'ㅁ 2획 (상우 꺾음)', 'type': 'corner', 'points': [[20, 20], [80, 20], [80, 80]]},
        {'name': 'ㅁ 3획 (하단 가로)', 'type': 'line', 'points': [[20, 80], [80, 80]]}
    ],
    'ㅂ': [
        {'name': 'ㅂ 1획 (좌측 세로)', 'type': 'line', 'points': [[20, 15], [20, 80]]},
        {'name': 'ㅂ 2획 (우측 세로)', 'type': 'line', 'points': [[80, 15], [80, 80]]},
        {'name': 'ㅂ 3획 (중간 가로)', 'type': 'line', 'points': [[20, 50], [80, 50]]},
        {'name': 'ㅂ 4획 (하단 가로)', 'type': 'line', 'points': [[20, 80], [80, 80]]}
    ],
    'ㅃ': [
        {'name': '첫 ㅂ 1획', 'type': 'line', 'points': [[10, 15], [10, 80]]},
        {'name': '첫 ㅂ 2획', 'type': 'line', 'points': [[45, 15], [45, 80]]},
        {'name': '첫 ㅂ 3획', 'type': 'line', 'points': [[10, 50], [45, 50]]},
        {'name': '첫 ㅂ 4획', 'type': 'line', 'points': [[10, 80], [45, 80]]},
        {'name': '둘째 ㅂ 1획', 'type': 'line', 'points': [[55, 15], [55, 80]]},
        {'name': '둘째 ㅂ 2획', 'type': 'line', 'points': [[90, 15], [90, 80]]},
        {'name': '둘째 ㅂ 3획', 'type': 'line', 'points': [[55, 50], [90, 50]]},
        {'name': '둘째 ㅂ 4획', 'type': 'line', 'points': [[55, 80], [90, 80]]}
    ],
    'ㅅ': [
        {'name': 'ㅅ 1획 (좌측 빗침)', 'type': 'line', 'points': [[50, 15], [20, 85]]},
        {'name': 'ㅅ 2획 (우측 빗침)', 'type': 'line', 'points': [[45, 45], [80, 85]]}
    ],
    'ㅆ': [
        {'name': '첫 ㅅ 1획', 'type': 'line', 'points': [[30, 15], [10, 85]]},
        {'name': '첫 ㅅ 2획', 'type': 'line', 'points': [[25, 45], [45, 85]]},
        {'name': '둘째 ㅅ 1획', 'type': 'line', 'points': [[70, 15], [55, 85]]},
        {'name': '둘째 ㅅ 2획', 'type': 'line', 'points': [[65, 45], [90, 85]]}
    ],
    'ㅇ': [
        {'name': 'ㅇ 1획 (원형 획순)', 'type': 'circle', 'points': [
            [50, 15], [20, 35], [20, 65], [50, 85], [80, 65], [80, 35], [50, 15]
        ]}
    ],
    'ㅈ': [
        {'name': 'ㅈ 1획 (상단 가로)', 'type': 'line', 'points': [[20, 20], [80, 20]]},
        {'name': 'ㅈ 2획 (좌측 빗침)', 'type': 'line', 'points': [[50, 20], [20, 85]]},
        {'name': 'ㅈ 3획 (우측 빗침)', 'type': 'line', 'points': [[45, 45], [80, 85]]}
    ],
    'ㅉ': [
        {'name': '첫 ㅈ 1획', 'type': 'line', 'points': [[10, 20], [45, 20]]},
        {'name': '첫 ㅈ 2획', 'type': 'line', 'points': [[28, 20], [10, 85]]},
        {'name': '첫 ㅈ 3획', 'type': 'line', 'points': [[24, 45], [45, 85]]},
        {'name': '둘째 ㅈ 1획', 'type': 'line', 'points': [[55, 20], [90, 20]]},
        {'name': '둘째 ㅈ 2획', 'type': 'line', 'points': [[73, 20], [55, 85]]},
        {'name': '둘째 ㅈ 3획', 'type': 'line', 'points': [[69, 45], [90, 85]]}
    ],
    'ㅊ': [
        {'name': 'ㅊ 1획 (상단 꼭지점)', 'type': 'line', 'points': [[50, 10], [50, 25]]},
        {'name': 'ㅊ 2획 (상단 가로)', 'type': 'line', 'points': [[20, 32], [80, 32]]},
        {'name': 'ㅊ 3획 (좌측 빗침)', 'type': 'line', 'points': [[50, 32], [20, 85]]},
        {'name': 'ㅊ 4획 (우측 빗침)', 'type': 'line', 'points': [[45, 52], [80, 85]]}
    ],
    'ㅋ': [
        {'name': 'ㅋ 1획 (ㄱ형태)', 'type': 'corner', 'points': [[20, 15], [80, 15], [80, 85]]},
        {'name': 'ㅋ 2획 (중간 가로)', 'type': 'line', 'points': [[20, 50], [75, 50]]}
    ],
    'ㅌ': [
        {'name': 'ㅌ 1획 (상단 가로)', 'type': 'line', 'points': [[20, 20], [80, 20]]},
        {'name': 'ㅌ 2획 (중간 가로)', 'type': 'line', 'points': [[20, 50], [75, 50]]},
        {'name': 'ㅌ 3획 (ㄴ형태)', 'type': 'corner', 'points': [[20, 20], [20, 80], [80, 80]]}
    ],
    'ㅍ': [
        {'name': 'ㅍ 1획 (상단 가로)', 'type': 'line', 'points': [[15, 20], [85, 20]]},
        {'name': 'ㅍ 2획 (좌측 세로)', 'type': 'line', 'points': [[35, 20], [35, 78]]},
        {'name': 'ㅍ 3획 (우측 세로)', 'type': 'line', 'points': [[65, 20], [65, 78]]},
        {'name': 'ㅍ 4획 (하단 가로)', 'type': 'line', 'points': [[15, 80], [85, 80]]}
    ],
    'ㅎ': [
        {'name': 'ㅎ 1획 (상단 짧은 가로)', 'type': 'line', 'points': [[40, 12], [60, 12]]},
        {'name': 'ㅎ 2획 (중간 긴 가로)', 'type': 'line', 'points': [[15, 30], [85, 30]]},
        {'name': 'ㅎ 3획 (하단 원)', 'type': 'circle', 'points': [
            [50, 45], [25, 60], [25, 75], [50, 90], [75, 75], [75, 60], [50, 45]
        ]}
    ],

    # Vowels
    'ㅏ': [
        {'name': 'ㅏ 1획 (세로)', 'type': 'line', 'points': [[50, 10], [50, 90]]},
        {'name': 'ㅏ 2획 (우측 점)', 'type': 'line', 'points': [[50, 50], [85, 50]]}
    ],
    'ㅑ': [
        {'name': 'ㅑ 1획 (세로)', 'type': 'line', 'points': [[40, 10], [40, 90]]},
        {'name': 'ㅑ 2획 (상우 점)', 'type': 'line', 'points': [[40, 35], [75, 35]]},
        {'name': 'ㅑ 3획 (하우 점)', 'type': 'line', 'points': [[40, 65], [75, 65]]}
    ],
    'ㅓ': [
        {'name': 'ㅓ 1획 (좌측 점)', 'type': 'line', 'points': [[15, 50], [50, 50]]},
        {'name': 'ㅓ 2획 (세로)', 'type': 'line', 'points': [[50, 10], [50, 90]]}
    ],
    'ㅕ': [
        {'name': 'ㅕ 1획 (상좌 점)', 'type': 'line', 'points': [[25, 35], [60, 35]]},
        {'name': 'ㅕ 2획 (하좌 점)', 'type': 'line', 'points': [[25, 65], [60, 65]]},
        {'name': 'ㅕ 3획 (세로)', 'type': 'line', 'points': [[60, 10], [60, 90]]}
    ],
    'ㅗ': [
        {'name': 'ㅗ 1획 (상단 세로점)', 'type': 'line', 'points': [[50, 15], [50, 55]]},
        {'name': 'ㅗ 2획 (가로)', 'type': 'line', 'points': [[10, 55], [90, 55]]}
    ],
    'ㅛ': [
        {'name': 'ㅛ 1획 (좌측 세로점)', 'type': 'line', 'points': [[35, 15], [35, 55]]},
        {'name': 'ㅛ 2획 (우측 세로점)', 'type': 'line', 'points': [[65, 15], [65, 55]]},
        {'name': 'ㅛ 3획 (가로)', 'type': 'line', 'points': [[10, 55], [90, 55]]}
    ],
    'ㅜ': [
        {'name': 'ㅜ 1획 (가로)', 'type': 'line', 'points': [[10, 45], [90, 45]]},
        {'name': 'ㅜ 2획 (하단 세로점)', 'type': 'line', 'points': [[50, 45], [50, 85]]}
    ],
    'ㅠ': [
        {'name': 'ㅠ 1획 (가로)', 'type': 'line', 'points': [[10, 45], [90, 45]]},
        {'name': 'ㅠ 2획 (좌측 세로점)', 'type': 'line', 'points': [[35, 45], [35, 85]]},
        {'name': 'ㅠ 3획 (우측 세로점)', 'type': 'line', 'points': [[65, 45], [65, 85]]}
    ],
    'ㅡ': [
        {'name': 'ㅡ 1획 (가로)', 'type': 'line', 'points': [[10, 50], [90, 50]]}
    ],
    'ㅣ': [
        {'name': 'ㅣ 1획 (세로)', 'type': 'line', 'points': [[50, 10], [50, 90]]}
    ],
    'ㅐ': [
        {'name': 'ㅐ 1획 (ㅏ세로)', 'type': 'line', 'points': [[30, 10], [30, 90]]},
        {'name': 'ㅐ 2획 (중간 가로)', 'type': 'line', 'points': [[30, 50], [70, 50]]},
        {'name': 'ㅐ 3획 (ㅣ세로)', 'type': 'line', 'points': [[70, 10], [70, 90]]}
    ],
    'ㅔ': [
        {'name': 'ㅔ 1획 (좌측 가로)', 'type': 'line', 'points': [[15, 50], [45, 50]]},
        {'name': 'ㅔ 2획 (ㅓ세로)', 'type': 'line', 'points': [[45, 10], [45, 90]]},
        {'name': 'ㅔ 3획 (ㅣ세로)', 'type': 'line', 'points': [[80, 10], [80, 90]]}
    ],
    'ㅘ': [
        {'name': 'ㅘ 1획 (ㅗ세로점)', 'type': 'line', 'points': [[25, 20], [25, 60]]},
        {'name': 'ㅘ 2획 (ㅗ가로)', 'type': 'line', 'points': [[10, 60], [60, 60]]},
        {'name': 'ㅘ 3획 (ㅏ세로)', 'type': 'line', 'points': [[70, 10], [70, 90]]},
        {'name': 'ㅘ 4획 (ㅏ가로점)', 'type': 'line', 'points': [[70, 50], [95, 50]]}
    ],
    'ㅢ': [
        {'name': 'ㅢ 1획 (ㅡ가로)', 'type': 'line', 'points': [[10, 65], [65, 65]]},
        {'name': 'ㅢ 2획 (ㅣ세로)', 'type': 'line', 'points': [[75, 10], [75, 90]]}
    ]
}

# Fill aliases for remaining complex vowels by composition if needed
if 'ㅙ' not in JAMO_STROKE_TEMPLATES:
    JAMO_STROKE_TEMPLATES['ㅙ'] = JAMO_STROKE_TEMPLATES['ㅘ'] + [{'name': 'ㅙ 5획 (추가세로)', 'type': 'line', 'points': [[90, 10], [90, 90]]}]
if 'ㅚ' not in JAMO_STROKE_TEMPLATES:
    JAMO_STROKE_TEMPLATES['ㅚ'] = JAMO_STROKE_TEMPLATES['ㅗ'] + [{'name': 'ㅚ 3획 (세로)', 'type': 'line', 'points': [[80, 10], [80, 90]]}]
if 'ㅝ' not in JAMO_STROKE_TEMPLATES:
    JAMO_STROKE_TEMPLATES['ㅝ'] = JAMO_STROKE_TEMPLATES['ㅜ'] + JAMO_STROKE_TEMPLATES['ㅓ']
if 'ㅞ' not in JAMO_STROKE_TEMPLATES:
    JAMO_STROKE_TEMPLATES['ㅞ'] = JAMO_STROKE_TEMPLATES['ㅜ'] + JAMO_STROKE_TEMPLATES['ㅔ']
if 'ㅟ' not in JAMO_STROKE_TEMPLATES:
    JAMO_STROKE_TEMPLATES['ㅟ'] = JAMO_STROKE_TEMPLATES['ㅜ'] + [{'name': 'ㅟ 3획 (세로)', 'type': 'line', 'points': [[80, 10], [80, 90]]}]
if 'ㅒ' not in JAMO_STROKE_TEMPLATES:
    JAMO_STROKE_TEMPLATES['ㅒ'] = JAMO_STROKE_TEMPLATES['ㅑ'] + [{'name': 'ㅒ 4획 (세로)', 'type': 'line', 'points': [[85, 10], [85, 90]]}]
if 'ㅖ' not in JAMO_STROKE_TEMPLATES:
    JAMO_STROKE_TEMPLATES['ㅖ'] = JAMO_STROKE_TEMPLATES['ㅕ'] + [{'name': 'ㅖ 4획 (세로)', 'type': 'line', 'points': [[85, 10], [85, 90]]}]


def decompose_hangul(char: str) -> Tuple[str, str, str]:
    """Decomposes a Hangul syllable into (choseong, jungseong, jongseong)."""
    code = ord(char) - HANGUL_BASE
    if code < 0 or code > 11171:
        raise ValueError(f"'{char}' is not a valid modern Hangul syllable.")
    
    cho_idx = code // 588
    jung_idx = (code % 588) // 28
    jong_idx = code % 28
    
    return CHOSUNG_LIST[cho_idx], JUNGSUNG_LIST[jung_idx], JONGSUNG_LIST[jong_idx]


def transform_points(points: List[List[float]], box: Dict[str, float]) -> List[List[float]]:
    """Transforms points from normalized (0..100) space into bounding box (x, y, w, h)."""
    bx, by, bw, bh = box['x'], box['y'], box['w'], box['h']
    transformed = []
    for pt in points:
        nx = bx + (pt[0] / 100.0) * bw
        ny = by + (pt[1] / 100.0) * bh
        transformed.append([round(nx, 1), round(ny, 1)])
    return transformed


def points_to_svg_path(points: List[List[float]], is_closed: bool = False) -> str:
    """Converts a list of points into an SVG path string."""
    if not points:
        return ""
    d = f"M {points[0][0]} {points[0][1]}"
    for pt in points[1:]:
        d += f" L {pt[0]} {pt[1]}"
    if is_closed:
        d += " Z"
    return d


class HangulStrokeGenerator:
    """Automated engine for generating and verifying Hangul stroke datasets."""

    def __init__(self, canvas_size: int = 500):
        self.canvas_size = canvas_size

    def get_layout_boxes(self, v_type: str, has_batchim: bool) -> Dict[str, Dict[str, float]]:
        """Calculates precise bounding boxes for 초성, 중성, 종성 based on structure."""
        S = self.canvas_size
        padding = S * 0.05
        inner_w = S - padding * 2
        inner_h = S - padding * 2

        if not has_batchim:
            if v_type == 'V':
                # CV_Vertical (e.g. 가, 나, 다)
                return {
                    'cho': {'x': padding, 'y': padding + inner_h * 0.1, 'w': inner_w * 0.48, 'h': inner_h * 0.8},
                    'jung': {'x': padding + inner_w * 0.52, 'y': padding, 'w': inner_w * 0.48, 'h': inner_h},
                    'jong': {'x': 0, 'y': 0, 'w': 0, 'h': 0}
                }
            elif v_type == 'H':
                # CV_Horizontal (e.g. 고, 노, 도)
                return {
                    'cho': {'x': padding + inner_w * 0.1, 'y': padding, 'w': inner_w * 0.8, 'h': inner_h * 0.46},
                    'jung': {'x': padding, 'y': padding + inner_h * 0.50, 'w': inner_w, 'h': inner_h * 0.48},
                    'jong': {'x': 0, 'y': 0, 'w': 0, 'h': 0}
                }
            else: # 'VH' (e.g. 과, 뇌, 의)
                return {
                    'cho': {'x': padding, 'y': padding, 'w': inner_w * 0.5, 'h': inner_h * 0.45},
                    'jung': {'x': padding, 'y': padding + inner_h * 0.45, 'w': inner_w, 'h': inner_h * 0.55},
                    'jong': {'x': 0, 'y': 0, 'w': 0, 'h': 0}
                }
        else:
            if v_type == 'V':
                # CVC_Vertical (e.g. 간, 달, 한)
                return {
                    'cho': {'x': padding, 'y': padding, 'w': inner_w * 0.48, 'h': inner_h * 0.48},
                    'jung': {'x': padding + inner_w * 0.52, 'y': padding, 'w': inner_w * 0.48, 'h': inner_h * 0.52},
                    'jong': {'x': padding + inner_w * 0.08, 'y': padding + inner_h * 0.54, 'w': inner_w * 0.84, 'h': inner_h * 0.44}
                }
            elif v_type == 'H':
                # CVC_Horizontal (e.g. 곤, 돌, 글)
                return {
                    'cho': {'x': padding + inner_w * 0.12, 'y': padding, 'w': inner_w * 0.76, 'h': inner_h * 0.33},
                    'jung': {'x': padding + inner_w * 0.05, 'y': padding + inner_h * 0.35, 'w': inner_w * 0.9, 'h': inner_h * 0.30},
                    'jong': {'x': padding + inner_w * 0.12, 'y': padding + inner_h * 0.67, 'w': inner_w * 0.76, 'h': inner_h * 0.33}
                }
            else: # 'VH' (e.g. 관, 광, 활)
                return {
                    'cho': {'x': padding, 'y': padding, 'w': inner_w * 0.48, 'h': inner_h * 0.33},
                    'jung': {'x': padding + inner_w * 0.1, 'y': padding + inner_h * 0.33, 'w': inner_w * 0.85, 'h': inner_h * 0.35},
                    'jong': {'x': padding + inner_w * 0.1, 'y': padding + inner_h * 0.68, 'w': inner_w * 0.8, 'h': inner_h * 0.32}
                }

    def generate_character_data(self, char: str) -> Dict[str, Any]:
        """Generates the full stroke sequence, medians, and metadata for a syllable."""
        cho, jung, jong = decompose_hangul(char)
        v_type = VOWEL_TYPE.get(jung, 'V')
        has_batchim = (jong != '')
        boxes = self.get_layout_boxes(v_type, has_batchim)

        strokes_data = []
        global_stroke_idx = 1

        # 1. 초성 획 추가
        cho_templates = JAMO_STROKE_TEMPLATES.get(cho, [])
        for t in cho_templates:
            pts = transform_points(t['points'], boxes['cho'])
            is_closed = (t.get('type') == 'circle')
            strokes_data.append({
                'order': global_stroke_idx,
                'part': '초성',
                'jamo': cho,
                'name': t['name'],
                'type': t['type'],
                'median': pts,
                'svg_path': points_to_svg_path(pts, is_closed)
            })
            global_stroke_idx += 1

        # 2. 중성 획 추가
        jung_templates = JAMO_STROKE_TEMPLATES.get(jung, [])
        for t in jung_templates:
            pts = transform_points(t['points'], boxes['jung'])
            is_closed = (t.get('type') == 'circle')
            strokes_data.append({
                'order': global_stroke_idx,
                'part': '중성',
                'jamo': jung,
                'name': t['name'],
                'type': t['type'],
                'median': pts,
                'svg_path': points_to_svg_path(pts, is_closed)
            })
            global_stroke_idx += 1

        # 3. 종성(받침) 획 추가
        if has_batchim:
            # Check for double final consonants (복합받침)
            DOUBLE_BATCHIM = {
                'ㄳ': ('ㄱ', 'ㅅ'), 'ㄵ': ('ㄴ', 'ㅈ'), 'ㄶ': ('ㄴ', 'ㅎ'),
                'ㄺ': ('ㄹ', 'ㄱ'), 'ㄻ': ('ㄹ', 'ㅁ'), 'ㄼ': ('ㄹ', 'ㅂ'),
                'ㄽ': ('ㄹ', 'ㅅ'), 'ㄾ': ('ㄹ', 'ㅌ'), 'ㄿ': ('ㄹ', 'ㅍ'),
                'ㅀ': ('ㄹ', 'ㅎ'), 'ㅄ': ('ㅂ', 'ㅅ')
            }
            if jong in DOUBLE_BATCHIM:
                j1, j2 = DOUBLE_BATCHIM[jong]
                # split jong box horizontally
                j_box = boxes['jong']
                b1 = {'x': j_box['x'], 'y': j_box['y'], 'w': j_box['w'] * 0.48, 'h': j_box['h']}
                b2 = {'x': j_box['x'] + j_box['w'] * 0.52, 'y': j_box['y'], 'w': j_box['w'] * 0.48, 'h': j_box['h']}
                for t in JAMO_STROKE_TEMPLATES.get(j1, []):
                    pts = transform_points(t['points'], b1)
                    strokes_data.append({
                        'order': global_stroke_idx, 'part': '종성1', 'jamo': j1,
                        'name': t['name'], 'type': t['type'], 'median': pts,
                        'svg_path': points_to_svg_path(pts, t.get('type') == 'circle')
                    })
                    global_stroke_idx += 1
                for t in JAMO_STROKE_TEMPLATES.get(j2, []):
                    pts = transform_points(t['points'], b2)
                    strokes_data.append({
                        'order': global_stroke_idx, 'part': '종성2', 'jamo': j2,
                        'name': t['name'], 'type': t['type'], 'median': pts,
                        'svg_path': points_to_svg_path(pts, t.get('type') == 'circle')
                    })
                    global_stroke_idx += 1
            else:
                jong_templates = JAMO_STROKE_TEMPLATES.get(jong, [])
                for t in jong_templates:
                    pts = transform_points(t['points'], boxes['jong'])
                    is_closed = (t.get('type') == 'circle')
                    strokes_data.append({
                        'order': global_stroke_idx,
                        'part': '종성',
                        'jamo': jong,
                        'name': t['name'],
                        'type': t['type'],
                        'median': pts,
                        'svg_path': points_to_svg_path(pts, is_closed)
                    })
                    global_stroke_idx += 1

        # 4. Automated Verification check
        verification = self.verify_character_data(char, strokes_data, cho, jung, jong)

        return {
            'character': char,
            'unicode': f"U+{ord(char):04X}",
            'decomposition': {'choseong': cho, 'jungseong': jung, 'jongseong': jong},
            'layout_type': f"{'CVC' if has_batchim else 'CV'}_{v_type}",
            'total_strokes': len(strokes_data),
            'verification': verification,
            'strokes': strokes_data
        }

    def verify_character_data(self, char: str, strokes: List[Dict], cho: str, jung: str, jong: str) -> Dict[str, Any]:
        """Automated QA verification against rule metrics."""
        issues = []
        if len(strokes) == 0:
            issues.append("획이 생성되지 않았습니다.")
        
        # Check order continuity
        for i, st in enumerate(strokes):
            if st['order'] != (i + 1):
                issues.append(f"획 번호 불연속: {st['order']} vs {i+1}")
            if len(st['median']) < 2:
                issues.append(f"획 좌표 결함 ({st['name']}): 점이 2개 미만입니다.")

        return {
            'passed': (len(issues) == 0),
            'stroke_count': len(strokes),
            'issues': issues
        }


def main():
    generator = HangulStrokeGenerator(canvas_size=500)
    sample_chars = ['가', '한', '글', '꽃', '꿈', '별']
    output_dir = os.path.join(os.path.dirname(__file__), 'generated_data')
    os.makedirs(output_dir, exist_ok=True)

    print(f"=== 한글 획순 자동 생성 & 검증 엔진 시작 ===")
    results = {}
    for char in sample_chars:
        data = generator.generate_character_data(char)
        filename = f"{char}_{data['unicode']}.json"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        status = "✅ 통과" if data['verification']['passed'] else "❌ 오류"
        print(f"[{status}] 글자: '{char}' | 분해: {data['decomposition']['choseong']}+{data['decomposition']['jungseong']}+{data['decomposition']['jongseong'] or '-'} | 총 {data['total_strokes']}획 | 파일: {filename}")
        results[char] = data

    print(f"\n생성 완료! 결과 저장 디렉토리: {output_dir}")


if __name__ == '__main__':
    main()
