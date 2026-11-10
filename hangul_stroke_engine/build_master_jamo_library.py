"""
Build Canonical Master Jamo Library (258 Standard Modular Parts)
===============================================================
Constructs the complete 6-archetype Hangul Beol Modular System:
  - 19 Initial Consonants (Cho) x 6 Structural Layouts (V1, V2, H1, H2, M1, M2) = 114 parts
  - 21 Medial Vowels (Jung) x 3 Beols (beol_1: no batchim, beol_2: standard batchim, beol_3: complex/adjusted) = 63 parts
  - 27 Final Consonants (Jong) x 3 Structural Layouts (V2: vertical, H2: horizontal, M2: compound) = 81 parts
Total: exactly 258 pristine standard modular components.
"""

import os
import json
from typing import Dict, List, Any

CHO_LIST = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
JUNG_LIST = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
JONG_LIST = ['ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

LAYOUT_DESCRIPTIONS = {
    'V1': '가형 (초성+세로모음, 무받침, 키가 큰 장방형)',
    'V2': '각형 (초성+세로모음+받침, 상단 축소 집약형)',
    'H1': '고형 (초성+가로모음, 무받침, 평방형 와이드형)',
    'H2': '물/글형 (초성+가로모음+받침, 3단 적층 초박형)',
    'M1': '과형 (초성+복합모음, 무받침, 좌상단 축소형)',
    'M2': '광형 (초성+복합모음+받침, 4분할 좌상단 최소형)'
}

BEOL_DESCRIPTIONS = {
    'beol_1': '무받침형 (전고 기둥 및 하단 표준 배치 / V1, H1, M1 대응)',
    'beol_2': '단순받침형 (받침 공간 확보를 위한 기둥 단축 및 중간 적층 배치 / V2, H2, M2 대응)',
    'beol_3': '복합/광폭보정형 (이중 세로모음 및 겹받침 결합 시 정밀 비례 보정형)'
}

JONG_LAYOUT_DESCRIPTIONS = {
    'V2': '세로모음 결합형 받침 (달, 별, 한 - 우측 기둥 조화 하단 배치)',
    'H2': '가로모음 결합형 받침 (물, 글, 꽃 - 전폭 지지 안정 평방형)',
    'M2': '복합모음 결합형 받침 (광, 꿩, 괄 - 복합요소 하단 균형 지지형)'
}


def generate_cho_modules() -> Dict[str, Dict[str, Any]]:
    modules = {}

    for cho in CHO_LIST:
        modules[cho] = {}
        for layout in ['V1', 'V2', 'H1', 'H2', 'M1', 'M2']:
            strokes = []
            
            # --- ㄱ ---
            if cho == 'ㄱ':
                if layout == 'V1': # calibrated '가'
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (곡선 꺾음)',
                        'clip_box': {'x': 50, 'y': 140, 'w': 470, 'h': 650},
                        'd': 'M 90 185 L 485 185 C 470 400 360 620 55 755', 'width': 105, 'duration': 0.65
                    })
                elif layout == 'V2': # calibrated '각'
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (상단 꺾음)',
                        'clip_box': {'x': 40, 'y': 90, 'w': 480, 'h': 490},
                        'd': 'M 80 145 L 475 145 C 475 320 340 490 55 560', 'width': 120, 'duration': 0.6
                    })
                elif layout == 'H1': # calibrated '고', '그'
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (와이드 직각 꺾음)',
                        'clip_box': {'x': 120, 'y': 130, 'w': 670, 'h': 580},
                        'd': 'M 130 185 L 725 185 C 725 340 725 500 680 680', 'width': 120, 'duration': 0.6
                    })
                elif layout == 'H2': # calibrated '글', '곡'
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (초박형 직각 꺾음)',
                        'clip_box': {'x': 135, 'y': 80, 'w': 640, 'h': 350},
                        'd': 'M 140 135 L 735 135 C 735 240 735 340 695 440', 'width': 115, 'duration': 0.6
                    })
                elif layout == 'M1': # calibrated '과', '귀'
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (좌상단 축소 꺾음)',
                        'clip_box': {'x': 80, 'y': 110, 'w': 480, 'h': 390},
                        'd': 'M 91 160 L 506 160 L 480 490', 'width': 105, 'duration': 0.6
                    })
                else: # M2 calibrated '광', '권'
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (좌상단 최소 꺾음)',
                        'clip_box': {'x': 80, 'y': 90, 'w': 480, 'h': 325},
                        'd': 'M 99 144 L 506 144 L 482 405', 'width': 110, 'duration': 0.55
                    })

            # --- ㄲ ---
            elif cho == 'ㄲ':
                if layout == 'H2': # calibrated '꽃', '꿈'
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㄱ',
                        'clip_box': {'x': 110, 'y': 80, 'w': 295, 'h': 315},
                        'd': 'M 115 122 L 365 122 C 375 220 360 320 310 395', 'width': 125, 'duration': 0.45
                    })
                    strokes.append({
                        'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㄱ',
                        'clip_box': {'x': 460, 'y': 80, 'w': 325, 'h': 315},
                        'd': 'M 460 122 L 745 122 C 755 220 740 320 690 395', 'width': 125, 'duration': 0.45
                    })
                elif layout in ('V1', 'V2', 'M1'):
                    w_s = 220 if layout == 'V2' else 240
                    y_t = 90 if layout == 'V2' else 140
                    h_s = 340 if layout == 'V2' else 460
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㄱ',
                        'clip_box': {'x': 40, 'y': y_t, 'w': w_s, 'h': h_s},
                        'd': f'M 55 {y_t+45} L {40+w_s-20} {y_t+45} L {40+w_s-45} {y_t+h_s-20}', 'width': 105, 'duration': 0.45
                    })
                    strokes.append({
                        'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㄱ',
                        'clip_box': {'x': 40 + w_s - 10, 'y': y_t, 'w': w_s, 'h': h_s},
                        'd': f'M {40+w_s+5} {y_t+45} L {40+2*w_s-30} {y_t+45} L {40+2*w_s-55} {y_t+h_s-20}', 'width': 105, 'duration': 0.45
                    })
                elif layout == 'M2': # calibrated '꿩'
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㄱ',
                        'clip_box': {'x': 80, 'y': 90, 'w': 245, 'h': 295},
                        'd': 'M 101 137 L 319 137 C 319 220 280 320 209 380', 'width': 105, 'duration': 0.45
                    })
                    strokes.append({
                        'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㄱ',
                        'clip_box': {'x': 325, 'y': 90, 'w': 255, 'h': 295},
                        'd': 'M 360 137 L 573 137 C 573 220 540 320 466 369', 'width': 105, 'duration': 0.45
                    })
                else: # H1
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㄱ',
                        'clip_box': {'x': 110, 'y': 110, 'w': 295, 'h': 440},
                        'd': 'M 115 152 L 365 152 C 375 250 360 350 310 430', 'width': 125, 'duration': 0.45
                    })
                    strokes.append({
                        'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㄱ',
                        'clip_box': {'x': 460, 'y': 110, 'w': 325, 'h': 440},
                        'd': 'M 460 152 L 745 152 C 755 250 740 350 690 430', 'width': 125, 'duration': 0.45
                    })

            # --- ㄴ ---
            elif cho == 'ㄴ':
                if layout == 'H2': # calibrated '눈', '는'
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (초박형 평형 꺾음)',
                        'clip_box': {'x': 135, 'y': 80, 'w': 645, 'h': 330},
                        'd': 'M 195 80 L 195 380 L 760 380', 'width': 120, 'duration': 0.55
                    })
                elif layout == 'V1':
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (세로-가로 꺾음)',
                        'clip_box': {'x': 80, 'y': 140, 'w': 460, 'h': 640},
                        'd': 'M 130 140 L 130 735 L 515 735', 'width': 115, 'duration': 0.65
                    })
                elif layout == 'V2':
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (상단 세로-가로 꺾음)',
                        'clip_box': {'x': 80, 'y': 90, 'w': 460, 'h': 490},
                        'd': 'M 130 90 L 130 545 L 515 545', 'width': 115, 'duration': 0.6
                    })
                elif layout == 'H1':
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (와이드 평형 꺾음)',
                        'clip_box': {'x': 130, 'y': 110, 'w': 660, 'h': 540},
                        'd': 'M 190 120 L 190 610 L 750 610', 'width': 120, 'duration': 0.65
                    })
                elif layout == 'M1':
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (좌상단 축소 꺾음)',
                        'clip_box': {'x': 80, 'y': 120, 'w': 450, 'h': 440},
                        'd': 'M 135 120 L 135 520 L 495 520', 'width': 110, 'duration': 0.55
                    })
                else: # M2
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (좌상단 최소 꺾음)',
                        'clip_box': {'x': 80, 'y': 85, 'w': 430, 'h': 320},
                        'd': 'M 135 85 L 135 380 L 485 380', 'width': 110, 'duration': 0.5
                    })

            # --- ㄷ ---
            elif cho == 'ㄷ':
                if layout == 'V1': # calibrated '다'
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                                    'clip_box': {'x': 80, 'y': 140, 'w': 450, 'h': 110}, 'd': 'M 90 185 L 510 185', 'width': 110, 'duration': 0.35})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                                    'clip_box': {'x': 80, 'y': 180, 'w': 460, 'h': 590}, 'd': 'M 134 180 L 134 715 L 525 715', 'width': 130, 'duration': 0.65})
                elif layout == 'V2': # calibrated '달'
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                                    'clip_box': {'x': 80, 'y': 90, 'w': 450, 'h': 110}, 'd': 'M 90 135 L 500 135', 'width': 110, 'duration': 0.35})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                                    'clip_box': {'x': 80, 'y': 130, 'w': 460, 'h': 450}, 'd': 'M 134 130 L 134 545 L 515 545', 'width': 120, 'duration': 0.55})
                elif layout == 'H2':
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                                    'clip_box': {'x': 140, 'y': 75, 'w': 620, 'h': 105}, 'd': 'M 145 120 L 735 120', 'width': 110, 'duration': 0.35})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                                    'clip_box': {'x': 140, 'y': 110, 'w': 630, 'h': 290}, 'd': 'M 195 110 L 195 370 L 745 370', 'width': 115, 'duration': 0.55})
                elif layout == 'H1':
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                                    'clip_box': {'x': 130, 'y': 110, 'w': 640, 'h': 110}, 'd': 'M 140 160 L 740 160', 'width': 115, 'duration': 0.4})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                                    'clip_box': {'x': 130, 'y': 150, 'w': 650, 'h': 490}, 'd': 'M 190 150 L 190 600 L 750 600', 'width': 120, 'duration': 0.65})
                elif layout == 'M1':
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                                    'clip_box': {'x': 80, 'y': 120, 'w': 440, 'h': 105}, 'd': 'M 90 160 L 490 160', 'width': 105, 'duration': 0.35})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                                    'clip_box': {'x': 80, 'y': 155, 'w': 450, 'h': 390}, 'd': 'M 135 155 L 135 510 L 500 510', 'width': 110, 'duration': 0.55})
                else: # M2
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                                    'clip_box': {'x': 80, 'y': 80, 'w': 420, 'h': 100}, 'd': 'M 90 120 L 475 120', 'width': 105, 'duration': 0.3})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                                    'clip_box': {'x': 80, 'y': 115, 'w': 430, 'h': 285}, 'd': 'M 135 115 L 135 370 L 485 370', 'width': 110, 'duration': 0.5})

            # --- ㄸ ---
            elif cho == 'ㄸ':
                w_unit = 210 if layout in ('V1', 'V2', 'M1', 'M2') else 310
                y_t = 85 if layout in ('V2', 'H2', 'M2') else 125
                h_s = 280 if layout in ('V2', 'H2', 'M2') else 440
                gap = 230 if layout in ('V1', 'V2', 'M1', 'M2') else 340
                x_b = 60 if layout in ('V1', 'V2', 'M1', 'M2') else 120

                for i, prefix in enumerate(['첫째 ㄷ', '둘째 ㄷ']):
                    off = i * gap
                    strokes.append({'rel_order': 2*i + 1, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 1획',
                                    'clip_box': {'x': x_b + off, 'y': y_t, 'w': w_unit, 'h': 95},
                                    'd': f'M {x_b + off + 10} {y_t + 40} L {x_b + off + w_unit - 15} {y_t + 40}', 'width': 105, 'duration': 0.3})
                    strokes.append({'rel_order': 2*i + 2, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 2획',
                                    'clip_box': {'x': x_b + off, 'y': y_t + 35, 'w': w_unit, 'h': h_s - 35},
                                    'd': f'M {x_b + off + 35} {y_t + 35} L {x_b + off + 35} {y_t + h_s - 20} L {x_b + off + w_unit - 10} {y_t + h_s - 20}', 'width': 110, 'duration': 0.5})

            # --- ㄹ ---
            elif cho == 'ㄹ':
                y_t = 85 if layout in ('V2', 'H2', 'M2') else 135
                h_s = 295 if layout in ('V2', 'H2', 'M2') else (550 if layout in ('V1', 'H1') else 420)
                x_l = 80 if layout in ('V1', 'V2', 'M1', 'M2') else 140
                w_s = 450 if layout in ('V1', 'V2', 'M1', 'M2') else 625
                y1 = y_t + int(h_s * 0.35)
                y2 = y_t + int(h_s * 0.65)

                strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 1획 (상단 ㄱ)',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': w_s, 'h': int(h_s * 0.45)},
                                'd': f'M {x_l + 10} {y_t + 40} L {x_l + w_s - 15} {y_t + 40} L {x_l + w_s - 25} {y1 + 10}', 'width': 105, 'duration': 0.5})
                strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 2획 (중간 가로)',
                                'clip_box': {'x': x_l, 'y': y1 - 20, 'w': w_s, 'h': int(h_s * 0.35)},
                                'd': f'M {x_l + 10} {y2 - 20} L {x_l + w_s - 10} {y2 - 20}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 3획 (하단 ㄴ)',
                                'clip_box': {'x': x_l, 'y': y2 - 25, 'w': w_s, 'h': h_s - (y2 - y_t) + 30},
                                'd': f'M {x_l + 40} {y2 - 25} L {x_l + 40} {y_t + h_s - 20} L {x_l + w_s - 10} {y_t + h_s - 20}', 'width': 110, 'duration': 0.6})

            # --- ㅁ ---
            elif cho == 'ㅁ':
                if layout == 'H2': # calibrated pristine '물'
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 1획 (좌측 세로)',
                                    'clip_box': {'x': 150, 'y': 83, 'w': 90, 'h': 285}, 'd': 'M 196 83 L 196 368', 'width': 105, 'duration': 0.4})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 2획 (상단-우측 꺾음)',
                                    'clip_box': {'x': 235, 'y': 83, 'w': 535, 'h': 285}, 'd': 'M 196 116 L 720 116 L 720 368', 'width': 105, 'duration': 0.55})
                    strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 3획 (하단 가로)',
                                    'clip_box': {'x': 235, 'y': 285, 'w': 450, 'h': 85}, 'd': 'M 196 326 L 720 326', 'width': 100, 'duration': 0.35})
                else:
                    y_t = 85 if layout in ('V2', 'M2') else 130
                    h_s = 290 if layout in ('V2', 'M2') else (520 if layout in ('V1', 'H1') else 400)
                    x_l = 80 if layout in ('V1', 'V2', 'M1', 'M2') else 140
                    w_s = 450 if layout in ('V1', 'V2', 'M1', 'M2') else 630

                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 1획 (좌측 세로)',
                                    'clip_box': {'x': x_l, 'y': y_t, 'w': 95, 'h': h_s}, 'd': f'M {x_l + 42} {y_t} L {x_l + 42} {y_t + h_s}', 'width': 105, 'duration': 0.4})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 2획 (상단-우측 꺾음)',
                                    'clip_box': {'x': x_l + 80, 'y': y_t, 'w': w_s - 80, 'h': h_s}, 'd': f'M {x_l + 42} {y_t + 35} L {x_l + w_s - 40} {y_t + 35} L {x_l + w_s - 40} {y_t + h_s}', 'width': 105, 'duration': 0.6})
                    strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 3획 (하단 가로)',
                                    'clip_box': {'x': x_l + 80, 'y': y_t + h_s - 75, 'w': w_s - 120, 'h': 75}, 'd': f'M {x_l + 42} {y_t + h_s - 35} L {x_l + w_s - 40} {y_t + h_s - 35}', 'width': 100, 'duration': 0.35})

            # --- ㅂ ---
            elif cho == 'ㅂ':
                if layout == 'V2': # calibrated pristine '별'
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 1획 (좌측 세로)',
                                    'clip_box': {'x': 90, 'y': 90, 'w': 92, 'h': 405}, 'd': 'M 135 90 L 135 495', 'width': 110, 'duration': 0.45})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 2획 (우측 세로)',
                                    'clip_box': {'x': 418, 'y': 90, 'w': 88, 'h': 405}, 'd': 'M 462 90 L 462 495', 'width': 110, 'duration': 0.45})
                    strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 3획 (중간 가로)',
                                    'clip_box': {'x': 175, 'y': 220, 'w': 250, 'h': 72}, 'd': 'M 172 256 L 425 256', 'width': 95, 'duration': 0.35})
                    strokes.append({'rel_order': 4, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 4획 (하단 가로)',
                                    'clip_box': {'x': 175, 'y': 420, 'w': 250, 'h': 72}, 'd': 'M 172 455 L 425 455', 'width': 95, 'duration': 0.35})
                elif layout == 'H2': # calibrated pristine '봄'
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 1획 (좌측 세로)',
                                    'clip_box': {'x': 140, 'y': 80, 'w': 95, 'h': 326}, 'd': 'M 190 80 L 190 406', 'width': 105, 'duration': 0.45})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 2획 (우측 세로)',
                                    'clip_box': {'x': 675, 'y': 80, 'w': 95, 'h': 326}, 'd': 'M 720 80 L 720 406', 'width': 105, 'duration': 0.45})
                    strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 3획 (중간 가로)',
                                    'clip_box': {'x': 230, 'y': 190, 'w': 450, 'h': 75}, 'd': 'M 190 227 L 720 227', 'width': 95, 'duration': 0.35})
                    strokes.append({'rel_order': 4, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 4획 (하단 가로)',
                                    'clip_box': {'x': 230, 'y': 335, 'w': 450, 'h': 75}, 'd': 'M 190 372 L 720 372', 'width': 95, 'duration': 0.35})
                else:
                    y_t = 85 if layout in ('M2',) else 130
                    h_s = 300 if layout in ('M2',) else (540 if layout in ('V1', 'H1') else 420)
                    x_l = 80 if layout in ('V1', 'M1', 'M2') else 140
                    w_s = 450 if layout in ('V1', 'M1', 'M2') else 630

                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 1획 (좌측 세로)',
                                    'clip_box': {'x': x_l, 'y': y_t, 'w': 95, 'h': h_s}, 'd': f'M {x_l + 45} {y_t} L {x_l + 45} {y_t + h_s}', 'width': 105, 'duration': 0.45})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 2획 (우측 세로)',
                                    'clip_box': {'x': x_l + w_s - 95, 'y': y_t, 'w': 95, 'h': h_s}, 'd': f'M {x_l + w_s - 45} {y_t} L {x_l + w_s - 45} {y_t + h_s}', 'width': 105, 'duration': 0.45})
                    strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 3획 (중간 가로)',
                                    'clip_box': {'x': x_l + 80, 'y': y_t + int(h_s * 0.4) - 35, 'w': w_s - 160, 'h': 75}, 'd': f'M {x_l + 45} {y_t + int(h_s * 0.4)} L {x_l + w_s - 45} {y_t + int(h_s * 0.4)}', 'width': 95, 'duration': 0.35})
                    strokes.append({'rel_order': 4, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 4획 (하단 가로)',
                                    'clip_box': {'x': x_l + 80, 'y': y_t + h_s - 75, 'w': w_s - 160, 'h': 75}, 'd': f'M {x_l + 45} {y_t + h_s - 35} L {x_l + w_s - 45} {y_t + h_s - 35}', 'width': 95, 'duration': 0.35})

            # --- ㅃ ---
            elif cho == 'ㅃ':
                w_unit = 210 if layout in ('V1', 'V2', 'M1', 'M2') else 310
                y_t = 85 if layout in ('V2', 'H2', 'M2') else 125
                h_s = 280 if layout in ('V2', 'H2', 'M2') else 430
                gap = 230 if layout in ('V1', 'V2', 'M1', 'M2') else 340
                x_b = 60 if layout in ('V1', 'V2', 'M1', 'M2') else 120

                for i, prefix in enumerate(['첫째 ㅂ', '둘째 ㅂ']):
                    off = i * gap
                    strokes.append({'rel_order': 4*i + 1, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 1획 (좌세로)',
                                    'clip_box': {'x': x_b + off, 'y': y_t, 'w': 75, 'h': h_s}, 'd': f'M {x_b + off + 35} {y_t} L {x_b + off + 35} {y_t + h_s}', 'width': 95, 'duration': 0.3})
                    strokes.append({'rel_order': 4*i + 2, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 2획 (우세로)',
                                    'clip_box': {'x': x_b + off + w_unit - 75, 'y': y_t, 'w': 75, 'h': h_s}, 'd': f'M {x_b + off + w_unit - 35} {y_t} L {x_b + off + w_unit - 35} {y_t + h_s}', 'width': 95, 'duration': 0.3})
                    strokes.append({'rel_order': 4*i + 3, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 3획 (중가로)',
                                    'clip_box': {'x': x_b + off + 60, 'y': y_t + int(h_s*0.4) - 30, 'w': w_unit - 120, 'h': 65}, 'd': f'M {x_b + off + 35} {y_t + int(h_s*0.4)} L {x_b + off + w_unit - 35} {y_t + int(h_s*0.4)}', 'width': 90, 'duration': 0.25})
                    strokes.append({'rel_order': 4*i + 4, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 4획 (하가로)',
                                    'clip_box': {'x': x_b + off + 60, 'y': y_t + h_s - 65, 'w': w_unit - 120, 'h': 65}, 'd': f'M {x_b + off + 35} {y_t + h_s - 30} L {x_b + off + w_unit - 35} {y_t + h_s - 30}', 'width': 90, 'duration': 0.25})

            # --- ㅅ ---
            elif cho == 'ㅅ':
                if layout == 'V2': # calibrated '산'
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 1획 (좌측 빗침)',
                                    'clip_box': {'x': 40, 'y': 90, 'w': 340, 'h': 490}, 'd': 'M 320 115 C 320 280 200 460 55 570', 'width': 120, 'duration': 0.55})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 2획 (우측 빗침)',
                                    'clip_box': {'x': 270, 'y': 240, 'w': 250, 'h': 340}, 'd': 'M 290 280 L 515 570', 'width': 120, 'duration': 0.5})
                else:
                    y_t = 85 if layout in ('H2', 'M2') else 135
                    h_s = 290 if layout in ('H2', 'M2') else (550 if layout in ('V1', 'H1') else 430)
                    cx = 320 if layout in ('V1', 'M1', 'M2') else 450
                    x_l = 55 if layout in ('V1', 'M1', 'M2') else 140
                    x_r = 520 if layout in ('V1', 'M1', 'M2') else 750

                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 1획 (좌측 빗침)',
                                    'clip_box': {'x': x_l - 20, 'y': y_t, 'w': cx - x_l + 40, 'h': h_s},
                                    'd': f'M {cx} {y_t + 25} C {cx} {y_t + int(h_s*0.4)} {x_l + int((cx-x_l)*0.4)} {y_t + int(h_s*0.8)} {x_l} {y_t + h_s - 15}', 'width': 115, 'duration': 0.55})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 2획 (우측 빗침)',
                                    'clip_box': {'x': cx - 40, 'y': y_t + int(h_s*0.3), 'w': x_r - cx + 50, 'h': int(h_s*0.7)},
                                    'd': f'M {cx - 20} {y_t + int(h_s*0.4)} L {x_r} {y_t + h_s - 15}', 'width': 115, 'duration': 0.5})

            # --- ㅆ ---
            elif cho == 'ㅆ':
                w_unit = 210 if layout in ('V1', 'V2', 'M1', 'M2') else 310
                y_t = 85 if layout in ('V2', 'H2', 'M2') else 125
                h_s = 280 if layout in ('V2', 'H2', 'M2') else 430
                gap = 230 if layout in ('V1', 'V2', 'M1', 'M2') else 340
                x_b = 60 if layout in ('V1', 'V2', 'M1', 'M2') else 120

                for i, prefix in enumerate(['첫째 ㅅ', '둘째 ㅅ']):
                    off = i * gap
                    cx = x_b + off + int(w_unit * 0.6)
                    strokes.append({'rel_order': 2*i + 1, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 1획 (좌빗침)',
                                    'clip_box': {'x': x_b + off - 15, 'y': y_t, 'w': int(w_unit*0.65), 'h': h_s},
                                    'd': f'M {cx} {y_t + 25} C {cx} {y_t + int(h_s*0.4)} {x_b + off + 30} {y_t + int(h_s*0.8)} {x_b + off} {y_t + h_s - 15}', 'width': 105, 'duration': 0.45})
                    strokes.append({'rel_order': 2*i + 2, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 2획 (우빗침)',
                                    'clip_box': {'x': cx - 35, 'y': y_t + int(h_s*0.3), 'w': int(w_unit*0.55), 'h': int(h_s*0.7)},
                                    'd': f'M {cx - 20} {y_t + int(h_s*0.4)} L {x_b + off + w_unit} {y_t + h_s - 15}', 'width': 105, 'duration': 0.4})

            # --- ㅇ ---
            elif cho == 'ㅇ':
                if layout == 'V1': # calibrated '이'
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (원형 폐곡선)',
                        'clip_box': {'x': 70, 'y': 150, 'w': 460, 'h': 620},
                        'd': 'M 300 185 A 200 240 0 1 0 300 665 A 200 240 0 1 0 300 185', 'width': 115, 'duration': 0.8
                    })
                elif layout == 'V2':
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (상단 원형 폐곡선)',
                        'clip_box': {'x': 70, 'y': 90, 'w': 460, 'h': 480},
                        'd': 'M 300 125 A 200 190 0 1 0 300 505 A 200 190 0 1 0 300 125', 'width': 115, 'duration': 0.75
                    })
                elif layout == 'H1':
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (와이드 원형 폐곡선)',
                        'clip_box': {'x': 140, 'y': 110, 'w': 620, 'h': 540},
                        'd': 'M 450 145 A 270 215 0 1 0 450 575 A 270 215 0 1 0 450 145', 'width': 120, 'duration': 0.8
                    })
                elif layout == 'H2':
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (초박형 원형 폐곡선)',
                        'clip_box': {'x': 140, 'y': 80, 'w': 620, 'h': 320},
                        'd': 'M 450 105 A 270 125 0 1 0 450 355 A 270 125 0 1 0 450 105', 'width': 115, 'duration': 0.7
                    })
                elif layout == 'M1':
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (좌상단 축소 원형)',
                        'clip_box': {'x': 80, 'y': 120, 'w': 440, 'h': 420},
                        'd': 'M 300 155 A 190 165 0 1 0 300 485 A 190 165 0 1 0 300 155', 'width': 110, 'duration': 0.7
                    })
                else: # M2
                    strokes.append({
                        'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (좌상단 최소 원형)',
                        'clip_box': {'x': 80, 'y': 80, 'w': 420, 'h': 305},
                        'd': 'M 290 105 A 180 120 0 1 0 290 345 A 180 120 0 1 0 290 105', 'width': 105, 'duration': 0.65
                    })

            # --- ㅈ ---
            elif cho == 'ㅈ':
                y_t = 85 if layout in ('V2', 'H2', 'M2') else 135
                h_s = 290 if layout in ('V2', 'H2', 'M2') else (550 if layout in ('V1', 'H1') else 430)
                cx = 300 if layout in ('V1', 'V2', 'M1', 'M2') else 450
                x_l = 60 if layout in ('V1', 'V2', 'M1', 'M2') else 140
                x_r = 520 if layout in ('V1', 'V2', 'M1', 'M2') else 750

                strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 1획 (가로-좌빗침 꺾음)',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': x_r - x_l, 'h': h_s},
                                'd': f'M {x_l + 15} {y_t + 35} L {x_r - 15} {y_t + 35} L {cx} {y_t + int(h_s*0.35)} C {cx} {y_t + int(h_s*0.6)} {x_l + 40} {y_t + int(h_s*0.85)} {x_l + 10} {y_t + h_s - 15}', 'width': 110, 'duration': 0.65})
                strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 2획 (우측 빗침)',
                                'clip_box': {'x': cx - 20, 'y': y_t + int(h_s*0.25), 'w': x_r - cx + 25, 'h': int(h_s*0.75)},
                                'd': f'M {cx} {y_t + int(h_s*0.35)} L {x_r - 10} {y_t + h_s - 15}', 'width': 110, 'duration': 0.5})

            # --- ㅉ ---
            elif cho == 'ㅉ':
                w_unit = 210 if layout in ('V1', 'V2', 'M1', 'M2') else 310
                y_t = 85 if layout in ('V2', 'H2', 'M2') else 125
                h_s = 280 if layout in ('V2', 'H2', 'M2') else 430
                gap = 230 if layout in ('V1', 'V2', 'M1', 'M2') else 340
                x_b = 60 if layout in ('V1', 'V2', 'M1', 'M2') else 120

                for i, prefix in enumerate(['첫째 ㅈ', '둘째 ㅈ']):
                    off = i * gap
                    cx = x_b + off + int(w_unit * 0.5)
                    strokes.append({'rel_order': 2*i + 1, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 1획 (가로-좌빗침)',
                                    'clip_box': {'x': x_b + off, 'y': y_t, 'w': w_unit, 'h': h_s},
                                    'd': f'M {x_b + off + 10} {y_t + 35} L {x_b + off + w_unit - 10} {y_t + 35} L {cx} {y_t + int(h_s*0.35)} C {cx} {y_t + int(h_s*0.6)} {x_b + off + 25} {y_t + int(h_s*0.85)} {x_b + off} {y_t + h_s - 15}', 'width': 100, 'duration': 0.5})
                    strokes.append({'rel_order': 2*i + 2, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 2획 (우빗침)',
                                    'clip_box': {'x': cx - 20, 'y': y_t + int(h_s*0.25), 'w': int(w_unit*0.6), 'h': int(h_s*0.75)},
                                    'd': f'M {cx} {y_t + int(h_s*0.35)} L {x_b + off + w_unit} {y_t + h_s - 15}', 'width': 100, 'duration': 0.4})

            # --- ㅊ ---
            elif cho == 'ㅊ':
                if layout == 'H2': # calibrated '꽃'
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 1획 (상단 꼭지점)',
                                    'clip_box': {'x': 410, 'y': 50, 'w': 95, 'h': 85}, 'd': 'M 457 50 L 457 125', 'width': 95, 'duration': 0.3})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 2획 (중간 가로)',
                                    'clip_box': {'x': 140, 'y': 110, 'w': 635, 'h': 75}, 'd': 'M 145 145 L 760 145', 'width': 95, 'duration': 0.4})
                    strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 3획 (좌측 빗침)',
                                    'clip_box': {'x': 110, 'y': 150, 'w': 365, 'h': 240}, 'd': 'M 455 150 C 400 240 270 320 125 385', 'width': 120, 'duration': 0.5})
                    strokes.append({'rel_order': 4, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 4획 (우측 빗침)',
                                    'clip_box': {'x': 440, 'y': 150, 'w': 365, 'h': 240}, 'd': 'M 450 150 C 515 240 645 320 780 385', 'width': 120, 'duration': 0.5})
                else:
                    y_t = 65 if layout in ('V2', 'M2') else 105
                    h_s = 310 if layout in ('V2', 'M2') else (580 if layout in ('V1', 'H1') else 440)
                    cx = 300 if layout in ('V1', 'V2', 'M1', 'M2') else 450
                    x_l = 60 if layout in ('V1', 'V2', 'M1', 'M2') else 140
                    x_r = 520 if layout in ('V1', 'V2', 'M1', 'M2') else 750

                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 1획 (상단 꼭지)',
                                    'clip_box': {'x': cx - 50, 'y': y_t, 'w': 100, 'h': 85}, 'd': f'M {cx} {y_t} L {cx} {y_t + 75}', 'width': 95, 'duration': 0.3})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 2획 (가로선)',
                                    'clip_box': {'x': x_l, 'y': y_t + 65, 'w': x_r - x_l, 'h': 75}, 'd': f'M {x_l + 15} {y_t + 100} L {x_r - 15} {y_t + 100}', 'width': 105, 'duration': 0.4})
                    strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 3획 (좌측 빗침)',
                                    'clip_box': {'x': x_l - 10, 'y': y_t + 100, 'w': cx - x_l + 25, 'h': h_s - 100},
                                    'd': f'M {cx} {y_t + 100} C {cx} {y_t + int(h_s*0.5)} {x_l + 40} {y_t + int(h_s*0.8)} {x_l + 10} {y_t + h_s - 15}', 'width': 115, 'duration': 0.55})
                    strokes.append({'rel_order': 4, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 4획 (우측 빗침)',
                                    'clip_box': {'x': cx - 20, 'y': y_t + 100, 'w': x_r - cx + 30, 'h': h_s - 100},
                                    'd': f'M {cx} {y_t + 100} L {x_r - 10} {y_t + h_s - 15}', 'width': 115, 'duration': 0.5})

            # --- ㅋ ---
            elif cho == 'ㅋ':
                y_t = 85 if layout in ('V2', 'H2', 'M2') else 135
                h_s = 290 if layout in ('V2', 'H2', 'M2') else (550 if layout in ('V1', 'H1') else 430)
                x_l = 60 if layout in ('V1', 'V2', 'M1', 'M2') else 140
                x_r = 510 if layout in ('V1', 'V2', 'M1', 'M2') else 740

                strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅋ 1획 (ㄱ 꺾음)',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': x_r - x_l + 20, 'h': h_s}, 'd': f'M {x_l + 15} {y_t + 40} L {x_r} {y_t + 40} L {x_r - 20} {y_t + h_s - 15}', 'width': 110, 'duration': 0.6})
                strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅋ 2획 (중간 가로)',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_s*0.4) - 35, 'w': x_r - x_l, 'h': 75}, 'd': f'M {x_l + 15} {y_t + int(h_s*0.4)} L {x_r - 20} {y_t + int(h_s*0.4)}', 'width': 105, 'duration': 0.35})

            # --- ㅌ ---
            elif cho == 'ㅌ':
                y_t = 85 if layout in ('V2', 'H2', 'M2') else 135
                h_s = 290 if layout in ('V2', 'H2', 'M2') else (550 if layout in ('V1', 'H1') else 430)
                x_l = 60 if layout in ('V1', 'V2', 'M1', 'M2') else 140
                x_r = 510 if layout in ('V1', 'V2', 'M1', 'M2') else 740

                strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 1획 (상단 가로)',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': x_r - x_l + 10, 'h': 85}, 'd': f'M {x_l + 15} {y_t + 40} L {x_r} {y_t + 40}', 'width': 110, 'duration': 0.35})
                strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 2획 (중간 가로)',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_s*0.45) - 35, 'w': x_r - x_l, 'h': 75}, 'd': f'M {x_l + 15} {y_t + int(h_s*0.45)} L {x_r - 10} {y_t + int(h_s*0.45)}', 'width': 105, 'duration': 0.35})
                strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 3획 (하단 ㄴ 꺾음)',
                                'clip_box': {'x': x_l, 'y': y_t + 50, 'w': x_r - x_l + 15, 'h': h_s - 50}, 'd': f'M {x_l + 55} {y_t + 50} L {x_l + 55} {y_t + h_s - 25} L {x_r + 5} {y_t + h_s - 25}', 'width': 115, 'duration': 0.6})

            # --- ㅍ ---
            elif cho == 'ㅍ':
                y_t = 85 if layout in ('V2', 'H2', 'M2') else 135
                h_s = 290 if layout in ('V2', 'H2', 'M2') else (550 if layout in ('V1', 'H1') else 430)
                x_l = 60 if layout in ('V1', 'V2', 'M1', 'M2') else 140
                x_r = 510 if layout in ('V1', 'V2', 'M1', 'M2') else 740
                col_w = int((x_r - x_l) * 0.3)

                strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 1획 (상단 가로)',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': x_r - x_l + 15, 'h': 85}, 'd': f'M {x_l + 10} {y_t + 40} L {x_r + 5} {y_t + 40}', 'width': 110, 'duration': 0.35})
                strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 2획 (좌측 세로)',
                                'clip_box': {'x': x_l + col_w - 40, 'y': y_t + 25, 'w': 80, 'h': h_s - 25}, 'd': f'M {x_l + col_w} {y_t + 30} L {x_l + col_w} {y_t + h_s - 25}', 'width': 105, 'duration': 0.4})
                strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 3획 (우측 세로)',
                                'clip_box': {'x': x_r - col_w - 40, 'y': y_t + 25, 'w': 80, 'h': h_s - 25}, 'd': f'M {x_r - col_w} {y_t + 30} L {x_r - col_w} {y_t + h_s - 25}', 'width': 105, 'duration': 0.4})
                strokes.append({'rel_order': 4, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 4획 (하단 가로)',
                                'clip_box': {'x': x_l, 'y': y_t + h_s - 65, 'w': x_r - x_l + 15, 'h': 75}, 'd': f'M {x_l + 10} {y_t + h_s - 25} L {x_r + 5} {y_t + h_s - 25}', 'width': 110, 'duration': 0.35})

            # --- ㅎ ---
            elif cho == 'ㅎ':
                if layout == 'V2': # calibrated '한'
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 1획 (상단 꼭지점)',
                                    'clip_box': {'x': 270, 'y': 50, 'w': 95, 'h': 118}, 'd': 'M 319 50 L 319 168', 'width': 105, 'duration': 0.3})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 2획 (중간 가로획)',
                                    'clip_box': {'x': 45, 'y': 155, 'w': 550, 'h': 85}, 'd': 'M 45 197 L 595 197', 'width': 105, 'duration': 0.45})
                    strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 3획 (원형 폐곡선)',
                                    'clip_box': {'x': 95, 'y': 270, 'w': 450, 'h': 355}, 'd': 'M 319 312 A 177 136 0 1 0 319 584 A 177 136 0 1 0 319 312', 'width': 120, 'duration': 0.75})
                elif layout == 'M2': # calibrated for M2 (e.g., '황')
                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 1획 (상단 꼭지점)',
                                    'clip_box': {'x': 287, 'y': 46, 'w': 82, 'h': 85}, 'd': 'M 327 46 L 327 131', 'width': 95, 'duration': 0.3})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 2획 (중간 가로획)',
                                    'clip_box': {'x': 60, 'y': 120, 'w': 535, 'h': 75}, 'd': 'M 68 162 L 587 162', 'width': 105, 'duration': 0.45})
                    strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 3획 (원형 폐곡선)',
                                    'clip_box': {'x': 110, 'y': 225, 'w': 435, 'h': 265}, 'd': 'M 327 259 A 171 100 0 1 0 327 459 A 171 100 0 1 0 327 259', 'width': 115, 'duration': 0.75})
                else:
                    y_t = 65 if layout == 'H2' else 105
                    cx = 300 if layout in ('V1', 'M1') else 450
                    x_l = 60 if layout in ('V1', 'M1') else 140
                    x_r = 520 if layout in ('V1', 'M1') else 750
                    r_x = int((x_r - x_l) * 0.35)
                    r_y = 110 if layout == 'H2' else 160
                    y_c = y_t + 180 + r_y

                    strokes.append({'rel_order': 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 1획 (상단 꼭지점)',
                                    'clip_box': {'x': cx - 45, 'y': y_t, 'w': 90, 'h': 95}, 'd': f'M {cx} {y_t} L {cx} {y_t + 85}', 'width': 100, 'duration': 0.3})
                    strokes.append({'rel_order': 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 2획 (중간 가로획)',
                                    'clip_box': {'x': x_l, 'y': y_t + 75, 'w': x_r - x_l, 'h': 80}, 'd': f'M {x_l + 10} {y_t + 115} L {x_r - 10} {y_t + 115}', 'width': 105, 'duration': 0.4})
                    strokes.append({'rel_order': 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 3획 (원형 폐곡선)',
                                    'clip_box': {'x': cx - r_x - 30, 'y': y_t + 160, 'w': 2*r_x + 60, 'h': 2*r_y + 40},
                                    'd': f'M {cx} {y_c - r_y} A {r_x} {r_y} 0 1 0 {cx} {y_c + r_y} A {r_x} {r_y} 0 1 0 {cx} {y_c - r_y}', 'width': 115, 'duration': 0.75})

            # Total bounding box
            min_x = min(s['clip_box']['x'] for s in strokes)
            min_y = min(s['clip_box']['y'] for s in strokes)
            max_x = max(s['clip_box']['x'] + s['clip_box']['w'] for s in strokes)
            max_y = max(s['clip_box']['y'] + s['clip_box']['h'] for s in strokes)

            modules[cho][layout] = {
                'jamo': cho,
                'part': '초성',
                'layout': layout,
                'layout_desc': LAYOUT_DESCRIPTIONS[layout],
                'stroke_count': len(strokes),
                'bbox': {'x': min_x, 'y': min_y, 'w': max_x - min_x, 'h': max_y - min_y},
                'strokes': strokes
            }

    return modules


def generate_jung_modules() -> Dict[str, Dict[str, Any]]:
    modules = {}

    for jung in JUNG_LIST:
        modules[jung] = {}
        for beol in ['beol_1', 'beol_2', 'beol_3']:
            strokes = []
            
            # --- ㅏ ---
            if jung == 'ㅏ':
                if beol == 'beol_1': # calibrated '가'
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 1획 (세로 기둥)',
                                    'clip_box': {'x': 660, 'y': 45, 'w': 100, 'h': 920}, 'd': 'M 710 45 L 710 965', 'width': 110, 'duration': 0.6})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 2획 (우측 가로가지)',
                                    'clip_box': {'x': 745, 'y': 440, 'w': 150, 'h': 80}, 'd': 'M 745 480 L 895 480', 'width': 100, 'duration': 0.3})
                else: # calibrated '각', '한', '달', '산'
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 1획 (세로 기둥)',
                                    'clip_box': {'x': 660, 'y': 45, 'w': 100, 'h': 695}, 'd': 'M 710 45 L 710 740', 'width': 110, 'duration': 0.6})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 2획 (우측 가로가지)',
                                    'clip_box': {'x': 745, 'y': 345, 'w': 150, 'h': 80}, 'd': 'M 745 385 L 895 385', 'width': 100, 'duration': 0.3})

            # --- ㅐ ---
            elif jung == 'ㅐ':
                y_bot = 960 if beol == 'beol_1' else 740
                y_br = 480 if beol == 'beol_1' else 385
                x1, x2 = 610, 785
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅐ 1획 (첫째 세로기둥)',
                                'clip_box': {'x': x1 - 50, 'y': 45, 'w': 90, 'h': y_bot - 45}, 'd': f'M {x1} 45 L {x1} {y_bot}', 'width': 100, 'duration': 0.55})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅐ 2획 (가운데 가로가지)',
                                'clip_box': {'x': x1 + 10, 'y': y_br - 35, 'w': x2 - x1 - 20, 'h': 70}, 'd': f'M {x1} {y_br} L {x2} {y_br}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅐ 3획 (둘째 세로기둥)',
                                'clip_box': {'x': x2 - 40, 'y': 45, 'w': 100, 'h': y_bot - 45}, 'd': f'M {x2} 45 L {x2} {y_bot}', 'width': 105, 'duration': 0.55})

            # --- ㅑ ---
            elif jung == 'ㅑ':
                y_bot = 965 if beol == 'beol_1' else 740
                x_stem = 710
                y1 = 360 if beol == 'beol_1' else 280
                y2 = 560 if beol == 'beol_1' else 440
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅑ 1획 (세로 기둥)',
                                'clip_box': {'x': 660, 'y': 45, 'w': 100, 'h': y_bot - 45}, 'd': f'M {x_stem} 45 L {x_stem} {y_bot}', 'width': 110, 'duration': 0.6})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅑ 2획 (상단 가로가지)',
                                'clip_box': {'x': 745, 'y': y1 - 35, 'w': 150, 'h': 70}, 'd': f'M 745 {y1} L 895 {y1}', 'width': 100, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅑ 3획 (하단 가로가지)',
                                'clip_box': {'x': 745, 'y': y2 - 35, 'w': 150, 'h': 70}, 'd': f'M 745 {y2} L 895 {y2}', 'width': 100, 'duration': 0.3})

            # --- ㅒ ---
            elif jung == 'ㅒ':
                y_bot = 960 if beol == 'beol_1' else 740
                x1, x2 = 610, 785
                y1 = 360 if beol == 'beol_1' else 280
                y2 = 560 if beol == 'beol_1' else 440
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅒ 1획 (첫째 세로기둥)',
                                'clip_box': {'x': x1 - 50, 'y': 45, 'w': 90, 'h': y_bot - 45}, 'd': f'M {x1} 45 L {x1} {y_bot}', 'width': 100, 'duration': 0.55})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅒ 2획 (상단 가로가지)',
                                'clip_box': {'x': x1 + 10, 'y': y1 - 35, 'w': x2 - x1 - 20, 'h': 70}, 'd': f'M {x1} {y1} L {x2} {y1}', 'width': 95, 'duration': 0.28})
                strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅒ 3획 (하단 가로가지)',
                                'clip_box': {'x': x1 + 10, 'y': y2 - 35, 'w': x2 - x1 - 20, 'h': 70}, 'd': f'M {x1} {y2} L {x2} {y2}', 'width': 95, 'duration': 0.28})
                strokes.append({'rel_order': 4, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅒ 4획 (둘째 세로기둥)',
                                'clip_box': {'x': x2 - 40, 'y': 45, 'w': 100, 'h': y_bot - 45}, 'd': f'M {x2} 45 L {x2} {y_bot}', 'width': 105, 'duration': 0.55})

            # --- ㅓ ---
            elif jung == 'ㅓ':
                y_bot = 965 if beol == 'beol_1' else 740
                y_br = 480 if beol == 'beol_1' else 385
                x_stem = 710
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 1획 (좌측 가로가지)',
                                'clip_box': {'x': 525, 'y': y_br - 40, 'w': 150, 'h': 80}, 'd': f'M 525 {y_br} L 675 {y_br}', 'width': 100, 'duration': 0.3})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 2획 (세로 기둥)',
                                'clip_box': {'x': 660, 'y': 45, 'w': 100, 'h': y_bot - 45}, 'd': f'M {x_stem} 45 L {x_stem} {y_bot}', 'width': 110, 'duration': 0.6})

            # --- ㅔ ---
            elif jung == 'ㅔ':
                y_bot = 960 if beol == 'beol_1' else 740
                y_br = 480 if beol == 'beol_1' else 385
                x1, x2 = 610, 785
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅔ 1획 (좌측 가로가지)',
                                'clip_box': {'x': 445, 'y': y_br - 35, 'w': 140, 'h': 70}, 'd': f'M 445 {y_br} L 585 {y_br}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅔ 2획 (첫째 세로기둥)',
                                'clip_box': {'x': x1 - 50, 'y': 45, 'w': 90, 'h': y_bot - 45}, 'd': f'M {x1} 45 L {x1} {y_bot}', 'width': 100, 'duration': 0.55})
                strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅔ 3획 (둘째 세로기둥)',
                                'clip_box': {'x': x2 - 40, 'y': 45, 'w': 100, 'h': y_bot - 45}, 'd': f'M {x2} 45 L {x2} {y_bot}', 'width': 105, 'duration': 0.55})

            # --- ㅕ ---
            elif jung == 'ㅕ':
                if beol == 'beol_2': # calibrated '별'
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 1획 (상단 가로가지)',
                                    'clip_box': {'x': 503, 'y': 180, 'w': 208, 'h': 69}, 'd': 'M 500 214 L 711 214', 'width': 95, 'duration': 0.32})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 2획 (하단 가로가지)',
                                    'clip_box': {'x': 503, 'y': 344, 'w': 208, 'h': 70}, 'd': 'M 500 378 L 711 378', 'width': 95, 'duration': 0.32})
                    strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 3획 (긴 세로기둥)',
                                    'clip_box': {'x': 711, 'y': 50, 'w': 86, 'h': 480}, 'd': 'M 752 48 L 752 530', 'width': 110, 'duration': 0.55})
                else:
                    y_bot = 965
                    x_stem = 710
                    y1, y2 = 360, 560
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 1획 (상단 가로가지)',
                                    'clip_box': {'x': 503, 'y': y1 - 35, 'w': 175, 'h': 70}, 'd': f'M 500 {y1} L 680 {y1}', 'width': 95, 'duration': 0.3})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 2획 (하단 가로가지)',
                                    'clip_box': {'x': 503, 'y': y2 - 35, 'w': 175, 'h': 70}, 'd': f'M 500 {y2} L 680 {y2}', 'width': 95, 'duration': 0.3})
                    strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 3획 (세로 기둥)',
                                    'clip_box': {'x': 660, 'y': 45, 'w': 100, 'h': y_bot - 45}, 'd': f'M {x_stem} 45 L {x_stem} {y_bot}', 'width': 110, 'duration': 0.6})

            # --- ㅖ ---
            elif jung == 'ㅖ':
                y_bot = 960 if beol == 'beol_1' else 740
                x1, x2 = 610, 785
                y1 = 360 if beol == 'beol_1' else 240
                y2 = 560 if beol == 'beol_1' else 400
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅖ 1획 (상단 가로가지)',
                                'clip_box': {'x': 445, 'y': y1 - 35, 'w': 140, 'h': 70}, 'd': f'M 445 {y1} L 585 {y1}', 'width': 95, 'duration': 0.28})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅖ 2획 (하단 가로가지)',
                                'clip_box': {'x': 445, 'y': y2 - 35, 'w': 140, 'h': 70}, 'd': f'M 445 {y2} L 585 {y2}', 'width': 95, 'duration': 0.28})
                strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅖ 3획 (첫째 세로기둥)',
                                'clip_box': {'x': x1 - 50, 'y': 45, 'w': 90, 'h': y_bot - 45}, 'd': f'M {x1} 45 L {x1} {y_bot}', 'width': 100, 'duration': 0.55})
                strokes.append({'rel_order': 4, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅖ 4획 (둘째 세로기둥)',
                                'clip_box': {'x': x2 - 40, 'y': 45, 'w': 100, 'h': y_bot - 45}, 'd': f'M {x2} 45 L {x2} {y_bot}', 'width': 105, 'duration': 0.55})

            # --- ㅗ ---
            elif jung == 'ㅗ':
                if beol == 'beol_1': # calibrated '고'
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                                    'clip_box': {'x': 420, 'y': 439, 'w': 80, 'h': 323}, 'd': 'M 459 439 L 459 762', 'width': 95, 'duration': 0.35})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가운데 긴가로)',
                                    'clip_box': {'x': 40, 'y': 762, 'w': 835, 'h': 80}, 'd': 'M 40 798 L 875 798', 'width': 95, 'duration': 0.5})
                else: # calibrated '꽃', '봄', '곡' (H2)
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                                    'clip_box': {'x': 430, 'y': 285, 'w': 92, 'h': 155}, 'd': 'M 476 285 L 476 440', 'width': 95, 'duration': 0.3})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가운데 긴가로)',
                                    'clip_box': {'x': 40, 'y': 440, 'w': 835, 'h': 75}, 'd': 'M 40 474 L 875 474', 'width': 95, 'duration': 0.5})

            # --- ㅘ ---
            elif jung == 'ㅘ':
                if beol == 'beol_1': # calibrated pristine '과'
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                                    'clip_box': {'x': 210, 'y': 390, 'w': 120, 'h': 310}, 'd': 'M 273 390 L 273 695', 'width': 100, 'duration': 0.35})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가로선)',
                                    'clip_box': {'x': 30, 'y': 650, 'w': 590, 'h': 120}, 'd': 'M 35 712 L 610 712', 'width': 105, 'duration': 0.5})
                    strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 1획 (세로기둥)',
                                    'clip_box': {'x': 650, 'y': 45, 'w': 110, 'h': 925}, 'd': 'M 701 45 L 701 960', 'width': 105, 'duration': 0.6})
                    strokes.append({'rel_order': 4, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 2획 (우측가지)',
                                    'clip_box': {'x': 735, 'y': 420, 'w': 160, 'h': 95}, 'd': 'M 701 466 L 890 466', 'width': 105, 'duration': 0.3})
                else: # calibrated pristine '광' (M2)
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                                    'clip_box': {'x': 210, 'y': 290, 'w': 120, 'h': 210}, 'd': 'M 276 290 L 276 495', 'width': 105, 'duration': 0.3})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가로선)',
                                    'clip_box': {'x': 30, 'y': 440, 'w': 590, 'h': 130}, 'd': 'M 40 508 L 615 508', 'width': 105, 'duration': 0.45})
                    strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 1획 (세로기둥)',
                                    'clip_box': {'x': 660, 'y': 45, 'w': 105, 'h': 585}, 'd': 'M 712 45 L 712 625', 'width': 110, 'duration': 0.55})
                    strokes.append({'rel_order': 4, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 2획 (우측가지)',
                                    'clip_box': {'x': 740, 'y': 285, 'w': 155, 'h': 95}, 'd': 'M 712 334 L 890 334', 'width': 105, 'duration': 0.3})

            # --- ㅙ ---
            elif jung == 'ㅙ':
                y_bot = 960 if beol == 'beol_1' else 630
                y_h = 712 if beol == 'beol_1' else 508
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                                'clip_box': {'x': 180, 'y': y_h - 220, 'w': 100, 'h': 220}, 'd': f'M 230 {y_h - 220} L 230 {y_h - 15}', 'width': 100, 'duration': 0.3})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가로선)',
                                'clip_box': {'x': 30, 'y': y_h - 60, 'w': 520, 'h': 110}, 'd': f'M 35 {y_h} L 540 {y_h}', 'width': 100, 'duration': 0.45})
                strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅐ 1획 (첫째 기둥)',
                                'clip_box': {'x': 570, 'y': 45, 'w': 90, 'h': y_bot - 45}, 'd': f'M 615 45 L 615 {y_bot}', 'width': 100, 'duration': 0.55})
                strokes.append({'rel_order': 4, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅐ 2획 (가로가지)',
                                'clip_box': {'x': 625, 'y': int(y_bot*0.5) - 35, 'w': 130, 'h': 70}, 'd': f'M 615 {int(y_bot*0.5)} L 775 {int(y_bot*0.5)}', 'width': 95, 'duration': 0.28})
                strokes.append({'rel_order': 5, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅐ 3획 (둘째 기둥)',
                                'clip_box': {'x': 740, 'y': 45, 'w': 100, 'h': y_bot - 45}, 'd': f'M 785 45 L 785 {y_bot}', 'width': 105, 'duration': 0.55})

            # --- ㅚ ---
            elif jung == 'ㅚ':
                y_bot = 960 if beol == 'beol_1' else 630
                y_h = 712 if beol == 'beol_1' else 508
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                                'clip_box': {'x': 210, 'y': y_h - 220, 'w': 110, 'h': 220}, 'd': f'M 260 {y_h - 220} L 260 {y_h - 15}', 'width': 100, 'duration': 0.3})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가로선)',
                                'clip_box': {'x': 30, 'y': y_h - 60, 'w': 580, 'h': 110}, 'd': f'M 35 {y_h} L 600 {y_h}', 'width': 100, 'duration': 0.45})
                strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅣ (세로 기둥)',
                                'clip_box': {'x': 660, 'y': 45, 'w': 110, 'h': y_bot - 45}, 'd': f'M 710 45 L 710 {y_bot}', 'width': 110, 'duration': 0.6})

            # --- ㅛ ---
            elif jung == 'ㅛ':
                y_bar = 798 if beol == 'beol_1' else 474
                y_top = 439 if beol == 'beol_1' else 285
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅛ 1획 (좌측 세로점)',
                                'clip_box': {'x': 320, 'y': y_top, 'w': 80, 'h': y_bar - y_top + 10}, 'd': f'M 360 {y_top} L 360 {y_bar - 10}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅛ 2획 (우측 세로점)',
                                'clip_box': {'x': 520, 'y': y_top, 'w': 80, 'h': y_bar - y_top + 10}, 'd': f'M 560 {y_top} L 560 {y_bar - 10}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅛ 3획 (가운데 긴가로)',
                                'clip_box': {'x': 40, 'y': y_bar - 36, 'w': 835, 'h': 75}, 'd': f'M 40 {y_bar} L 875 {y_bar}', 'width': 95, 'duration': 0.5})

            # --- ㅜ ---
            elif jung == 'ㅜ':
                if beol == 'beol_1':
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가운데 긴가로)',
                                    'clip_box': {'x': 40, 'y': 510, 'w': 835, 'h': 75}, 'd': 'M 40 545 L 875 545', 'width': 95, 'duration': 0.5})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                                    'clip_box': {'x': 410, 'y': 545, 'w': 95, 'h': 310}, 'd': 'M 457 545 L 457 850', 'width': 105, 'duration': 0.4})
                else: # calibrated pristine '물', '꿈', '눈' (0px flange fix)
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가운데 긴가로)',
                                    'clip_box': {'x': 40, 'y': 430, 'w': 835, 'h': 75}, 'd': 'M 40 467 L 875 467', 'width': 95, 'duration': 0.5})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                                    'clip_box': {'x': 410, 'y': 501, 'w': 95, 'h': 88}, 'd': 'M 457 501 L 457 589', 'width': 105, 'duration': 0.3})

            # --- ㅝ ---
            elif jung == 'ㅝ':
                if beol == 'beol_2': # calibrated '권', '꿩' (M2)
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가로선)',
                                    'clip_box': {'x': 35, 'y': 375, 'w': 610, 'h': 110}, 'd': 'M 40 430 L 635 430', 'width': 100, 'duration': 0.45})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                                    'clip_box': {'x': 280, 'y': 440, 'w': 110, 'h': 240}, 'd': 'M 340 440 L 340 678', 'width': 100, 'duration': 0.3})
                    strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 1획 (가로가지)',
                                    'clip_box': {'x': 500, 'y': 530, 'w': 220, 'h': 85}, 'd': 'M 514 578 L 720 578', 'width': 95, 'duration': 0.28})
                    strokes.append({'rel_order': 4, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 2획 (세로기둥)',
                                    'clip_box': {'x': 700, 'y': 45, 'w': 105, 'h': 695}, 'd': 'M 752 45 L 752 737', 'width': 105, 'duration': 0.55})
                else:
                    y_bot = 960
                    y_h = 600
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가로선)',
                                    'clip_box': {'x': 40, 'y': y_h - 45, 'w': 570, 'h': 90}, 'd': f'M 40 {y_h} L 600 {y_h}', 'width': 100, 'duration': 0.45})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                                    'clip_box': {'x': 280, 'y': y_h, 'w': 100, 'h': 180}, 'd': f'M 330 {y_h} L 330 {y_h + 170}', 'width': 95, 'duration': 0.3})
                    strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 1획 (가로가지)',
                                    'clip_box': {'x': 530, 'y': int(y_bot*0.5) - 35, 'w': 140, 'h': 70}, 'd': f'M 530 {int(y_bot*0.5)} L 670 {int(y_bot*0.5)}', 'width': 95, 'duration': 0.28})
                    strokes.append({'rel_order': 4, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 2획 (세로기둥)',
                                    'clip_box': {'x': 660, 'y': 45, 'w': 110, 'h': y_bot - 45}, 'd': f'M 710 45 L 710 {y_bot}', 'width': 105, 'duration': 0.55})

            # --- ㅞ ---
            elif jung == 'ㅞ':
                y_bot = 960 if beol == 'beol_1' else 630
                y_h = 600 if beol == 'beol_1' else 480
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가로선)',
                                'clip_box': {'x': 40, 'y': y_h - 45, 'w': 520, 'h': 90}, 'd': f'M 40 {y_h} L 550 {y_h}', 'width': 100, 'duration': 0.45})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                                'clip_box': {'x': 250, 'y': y_h, 'w': 100, 'h': 180}, 'd': f'M 300 {y_h} L 300 {y_h + 170}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅔ 1획 (가로가지)',
                                'clip_box': {'x': 475, 'y': int(y_bot*0.5) - 35, 'w': 120, 'h': 70}, 'd': f'M 475 {int(y_bot*0.5)} L 595 {int(y_bot*0.5)}', 'width': 90, 'duration': 0.28})
                strokes.append({'rel_order': 4, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅔ 2획 (첫째 기둥)',
                                'clip_box': {'x': 570, 'y': 45, 'w': 90, 'h': y_bot - 45}, 'd': f'M 615 45 L 615 {y_bot}', 'width': 100, 'duration': 0.55})
                strokes.append({'rel_order': 5, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅔ 3획 (둘째 기둥)',
                                'clip_box': {'x': 740, 'y': 45, 'w': 100, 'h': y_bot - 45}, 'd': f'M 785 45 L 785 {y_bot}', 'width': 105, 'duration': 0.55})

            # --- ㅟ ---
            elif jung == 'ㅟ':
                if beol == 'beol_1': # calibrated pristine '귀'
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가로선)',
                                    'clip_box': {'x': 35, 'y': 445, 'w': 635, 'h': 115}, 'd': 'M 40 506 L 660 506', 'width': 100, 'duration': 0.45})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                                    'clip_box': {'x': 280, 'y': 530, 'w': 110, 'h': 390}, 'd': 'M 337 530 L 337 915', 'width': 100, 'duration': 0.35})
                    strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅣ (세로 기둥)',
                                    'clip_box': {'x': 700, 'y': 45, 'w': 110, 'h': 925}, 'd': 'M 756 45 L 756 965', 'width': 105, 'duration': 0.6})
                else:
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가로선)',
                                    'clip_box': {'x': 35, 'y': 400, 'w': 600, 'h': 100}, 'd': 'M 40 450 L 630 450', 'width': 100, 'duration': 0.45})
                    strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                                    'clip_box': {'x': 280, 'y': 450, 'w': 100, 'h': 220}, 'd': 'M 330 450 L 330 670', 'width': 95, 'duration': 0.3})
                    strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅣ (세로 기둥)',
                                    'clip_box': {'x': 660, 'y': 45, 'w': 110, 'h': 630}, 'd': 'M 710 45 L 710 675', 'width': 110, 'duration': 0.55})

            # --- ㅠ ---
            elif jung == 'ㅠ':
                y_bar = 545 if beol == 'beol_1' else 467
                y_len = 300 if beol == 'beol_1' else 110
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅠ 1획 (가운데 긴가로)',
                                'clip_box': {'x': 40, 'y': y_bar - 35, 'w': 835, 'h': 75}, 'd': f'M 40 {y_bar} L 875 {y_bar}', 'width': 95, 'duration': 0.5})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅠ 2획 (좌측 세로점)',
                                'clip_box': {'x': 320, 'y': y_bar, 'w': 80, 'h': y_len}, 'd': f'M 360 {y_bar} L 360 {y_bar + y_len}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅠ 3획 (우측 세로점)',
                                'clip_box': {'x': 520, 'y': y_bar, 'w': 80, 'h': y_len}, 'd': f'M 560 {y_bar} L 560 {y_bar + y_len}', 'width': 95, 'duration': 0.3})

            # --- ㅡ ---
            elif jung == 'ㅡ':
                if beol == 'beol_1': # calibrated '그'
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅡ (긴 가로선)',
                                    'clip_box': {'x': 40, 'y': 735, 'w': 835, 'h': 80}, 'd': 'M 40 770 L 875 770', 'width': 95, 'duration': 0.5})
                else: # calibrated '글', '는' (H2)
                    strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅡ (가운데 긴 가로)',
                                    'clip_box': {'x': 40, 'y': 390, 'w': 835, 'h': 70}, 'd': 'M 40 423 L 880 423', 'width': 95, 'duration': 0.5})

            # --- ㅢ ---
            elif jung == 'ㅢ':
                y_bar = 710 if beol == 'beol_1' else 480
                y_bot = 960 if beol == 'beol_1' else 630
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅡ (긴 가로선)',
                                'clip_box': {'x': 40, 'y': y_bar - 45, 'w': 580, 'h': 90}, 'd': f'M 40 {y_bar} L 600 {y_bar}', 'width': 100, 'duration': 0.45})
                strokes.append({'rel_order': 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅣ (세로 기둥)',
                                'clip_box': {'x': 660, 'y': 45, 'w': 110, 'h': y_bot - 45}, 'd': f'M 710 45 L 710 {y_bot}', 'width': 110, 'duration': 0.6})

            # --- ㅣ ---
            elif jung == 'ㅣ':
                y_bot = 965 if beol == 'beol_1' else 740
                strokes.append({'rel_order': 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅣ (세로 기둥)',
                                'clip_box': {'x': 660, 'y': 45, 'w': 110, 'h': y_bot - 45}, 'd': f'M 710 45 L 710 {y_bot}', 'width': 110, 'duration': 0.6})

            # Total bounding box
            min_x = min(s['clip_box']['x'] for s in strokes)
            min_y = min(s['clip_box']['y'] for s in strokes)
            max_x = max(s['clip_box']['x'] + s['clip_box']['w'] for s in strokes)
            max_y = max(s['clip_box']['y'] + s['clip_box']['h'] for s in strokes)

            modules[jung][beol] = {
                'jamo': jung,
                'part': '중성',
                'beol': beol,
                'beol_desc': BEOL_DESCRIPTIONS[beol],
                'stroke_count': len(strokes),
                'bbox': {'x': min_x, 'y': min_y, 'w': max_x - min_x, 'h': max_y - min_y},
                'strokes': strokes
            }

    return modules


def generate_jong_modules() -> Dict[str, Dict[str, Any]]:
    modules = {}

    for jong in JONG_LIST:
        modules[jong] = {}
        for layout in ['V2', 'H2', 'M2']:
            strokes = []
            
            # Coordinate bounds based on layout
            if layout == 'V2':
                x_l, x_r = 180, 800
                y_t, y_b = 580, 950
            elif layout == 'H2':
                x_l, x_r = 140, 790
                y_t, y_b = 589, 950
            else: # M2
                x_l, x_r = 150, 785
                y_t, y_b = 620, 950

            w_tot = x_r - x_l
            h_tot = y_b - y_t

            # --- ㄱ ---
            if jong == 'ㄱ':
                if layout == 'V2': # calibrated '각'
                    strokes.append({
                        'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄱ 받침 (직각 꺾음)',
                        'clip_box': {'x': 150, 'y': 610, 'w': 620, 'h': 360},
                        'd': 'M 155 659 L 715 659 L 715 965', 'width': 115, 'duration': 0.65
                    })
                elif layout == 'H2': # calibrated '곡'
                    strokes.append({
                        'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄱ 받침 (직각 꺾음)',
                        'clip_box': {'x': 130, 'y': 640, 'w': 645, 'h': 330},
                        'd': 'M 135 687 L 725 687 L 725 965', 'width': 115, 'duration': 0.65
                    })
                else: # M2
                    strokes.append({
                        'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄱ 받침 (직각 꺾음)',
                        'clip_box': {'x': x_l - 10, 'y': y_t, 'w': w_tot + 20, 'h': h_tot + 15},
                        'd': f'M {x_l} {y_t + 45} L {x_r - 10} {y_t + 45} L {x_r - 10} {y_b}', 'width': 120, 'duration': 0.65
                    })

            # --- ㄲ ---
            elif jong == 'ㄲ':
                w_half = int(w_tot * 0.48)
                gap = int(w_tot * 0.52)
                for i, prefix in enumerate(['첫째 ㄱ 받침', '둘째 ㄱ 받침']):
                    off = i * gap
                    strokes.append({
                        'rel_order': i + 1, 'part': '종성', 'color': '#10b981', 'name': prefix,
                        'clip_box': {'x': x_l + off - 10, 'y': y_t, 'w': w_half + 20, 'h': h_tot + 15},
                        'd': f'M {x_l + off} {y_t + 45} L {x_l + off + w_half - 15} {y_t + 45} L {x_l + off + w_half - 15} {y_b}', 'width': 110, 'duration': 0.45
                    })

            # --- ㄳ ---
            elif jong == 'ㄳ':
                w_g = int(w_tot * 0.48)
                x_s = x_l + int(w_tot * 0.52)
                w_s = x_r - x_s
                strokes.append({
                    'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄱ 받침 (꺾음)',
                    'clip_box': {'x': x_l - 10, 'y': y_t, 'w': w_g + 20, 'h': h_tot + 15},
                    'd': f'M {x_l} {y_t + 45} L {x_l + w_g - 15} {y_t + 45} L {x_l + w_g - 15} {y_b}', 'width': 105, 'duration': 0.45
                })
                cx = x_s + int(w_s * 0.5)
                strokes.append({
                    'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅅ 1획 (좌빗침)',
                    'clip_box': {'x': x_s - 10, 'y': y_t, 'w': cx - x_s + 15, 'h': h_tot + 15},
                    'd': f'M {cx} {y_t + 35} L {x_s} {y_b}', 'width': 105, 'duration': 0.4
                })
                strokes.append({
                    'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅅ 2획 (우빗침)',
                    'clip_box': {'x': cx - 15, 'y': y_t + int(h_tot*0.3), 'w': x_r - cx + 15, 'h': int(h_tot*0.7) + 15},
                    'd': f'M {cx - 10} {y_t + int(h_tot*0.35)} L {x_r} {y_b}', 'width': 105, 'duration': 0.4
                })

            # --- ㄴ ---
            elif jong == 'ㄴ':
                if layout == 'V2': # calibrated '한'
                    strokes.append({
                        'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄴ 받침 (세로-가로 꺾음)',
                        'clip_box': {'x': 180, 'y': 670, 'w': 620, 'h': 275},
                        'd': 'M 230 670 L 230 904 L 800 904', 'width': 110, 'duration': 0.65
                    })
                elif layout == 'H2': # calibrated '눈', '는'
                    strokes.append({
                        'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄴ 받침 (세로-가로 꺾음)',
                        'clip_box': {'x': 140, 'y': 650, 'w': 655, 'h': 295},
                        'd': 'M 195 650 L 195 904 L 795 904', 'width': 115, 'duration': 0.65
                    })
                else: # calibrated '권' (M2)
                    strokes.append({
                        'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄴ 받침 (세로-가로 꺾음)',
                        'clip_box': {'x': 160, 'y': 650, 'w': 665, 'h': 295},
                        'd': 'M 218 650 L 218 904 L 816 904', 'width': 110, 'duration': 0.65
                    })

            # --- ㄵ ---
            elif jong == 'ㄵ':
                w_n = int(w_tot * 0.48)
                x_j = x_l + int(w_tot * 0.52)
                w_j = x_r - x_j
                strokes.append({
                    'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄴ 받침 (꺾음)',
                    'clip_box': {'x': x_l - 10, 'y': y_t, 'w': w_n + 15, 'h': h_tot + 15},
                    'd': f'M {x_l + 35} {y_t + 10} L {x_l + 35} {y_b - 25} L {x_l + w_n} {y_b - 25}', 'width': 105, 'duration': 0.5
                })
                cx = x_j + int(w_j * 0.5)
                strokes.append({
                    'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅈ 1획 (가로-좌빗침)',
                    'clip_box': {'x': x_j - 10, 'y': y_t, 'w': w_j + 15, 'h': h_tot + 15},
                    'd': f'M {x_j} {y_t + 35} L {x_r} {y_t + 35} L {cx} {y_t + int(h_tot*0.35)} L {x_j} {y_b}', 'width': 100, 'duration': 0.5
                })
                strokes.append({
                    'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅈ 2획 (우빗침)',
                    'clip_box': {'x': cx - 15, 'y': y_t + int(h_tot*0.3), 'w': x_r - cx + 15, 'h': int(h_tot*0.7) + 15},
                    'd': f'M {cx} {y_t + int(h_tot*0.35)} L {x_r} {y_b}', 'width': 100, 'duration': 0.4
                })

            # --- ㄶ ---
            elif jong == 'ㄶ':
                w_n = int(w_tot * 0.48)
                x_h = x_l + int(w_tot * 0.52)
                w_h = x_r - x_h
                strokes.append({
                    'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄴ 받침 (꺾음)',
                    'clip_box': {'x': x_l - 10, 'y': y_t, 'w': w_n + 15, 'h': h_tot + 15},
                    'd': f'M {x_l + 35} {y_t + 10} L {x_l + 35} {y_b - 25} L {x_l + w_n} {y_b - 25}', 'width': 105, 'duration': 0.5
                })
                cx = x_h + int(w_h * 0.5)
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅎ 1획 (꼭지)',
                                'clip_box': {'x': cx - 35, 'y': y_t, 'w': 70, 'h': 65}, 'd': f'M {cx} {y_t} L {cx} {y_t + 55}', 'width': 95, 'duration': 0.25})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅎ 2획 (가로)',
                                'clip_box': {'x': x_h, 'y': y_t + 50, 'w': w_h, 'h': 65}, 'd': f'M {x_h} {y_t + 75} L {x_r} {y_t + 75}', 'width': 100, 'duration': 0.35})
                r_x = int(w_h * 0.38)
                r_y = int(h_tot * 0.25)
                y_c = y_b - r_y - 15
                strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅎ 3획 (원형)',
                                'clip_box': {'x': cx - r_x - 20, 'y': y_t + 105, 'w': 2*r_x + 40, 'h': 2*r_y + 30},
                                'd': f'M {cx} {y_c - r_y} A {r_x} {r_y} 0 1 0 {cx} {y_c + r_y} A {r_x} {r_y} 0 1 0 {cx} {y_c - r_y}', 'width': 105, 'duration': 0.6})

            # --- ㄷ ---
            elif jong == 'ㄷ':
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄷ 1획 (상단 가로)',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': w_tot, 'h': 85}, 'd': f'M {x_l + 15} {y_t + 40} L {x_r - 10} {y_t + 40}', 'width': 110, 'duration': 0.35})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                                'clip_box': {'x': x_l, 'y': y_t + 40, 'w': w_tot, 'h': h_tot - 25},
                                'd': f'M {x_l + 45} {y_t + 40} L {x_l + 45} {y_b - 25} L {x_r} {y_b - 25}', 'width': 115, 'duration': 0.6})

            # --- ㄹ ---
            elif jong == 'ㄹ':
                if layout == 'H2': # calibrated '물', '글' (0px flange fix)
                    strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 1획 (상단 ㄱ 꺾음)',
                                    'clip_box': {'x': 140, 'y': 589, 'w': 635, 'h': 151}, 'd': 'M 145 621 L 721 621 L 721 765', 'width': 110, 'duration': 0.5})
                    strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 2획 (중간 가로)',
                                    'clip_box': {'x': 140, 'y': 730, 'w': 635, 'h': 70}, 'd': 'M 145 762 L 775 762', 'width': 95, 'duration': 0.4})
                    strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 3획 (하단 ㄴ 꺾음)',
                                    'clip_box': {'x': 140, 'y': 785, 'w': 655, 'h': 175}, 'd': 'M 191 785 L 191 915 L 795 915', 'width': 110, 'duration': 0.65})
                elif layout == 'V2': # calibrated '별', '달'
                    strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 1획 (상단 ㄱ 꺾음)',
                                    'clip_box': {'x': 208, 'y': 565, 'w': 590, 'h': 160}, 'd': 'M 208 602 L 752 602 L 752 725', 'width': 105, 'duration': 0.5})
                    strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 2획 (중간 가로)',
                                    'clip_box': {'x': 210, 'y': 718, 'w': 588, 'h': 70}, 'd': 'M 210 752 L 795 752', 'width': 95, 'duration': 0.4})
                    strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 3획 (하단 ㄴ 꺾음)',
                                    'clip_box': {'x': 208, 'y': 780, 'w': 625, 'h': 172}, 'd': 'M 254 775 L 254 912 L 832 912', 'width': 110, 'duration': 0.65})
                else: # M2
                    strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 1획 (상단 ㄱ 꺾음)',
                                    'clip_box': {'x': 150, 'y': 620, 'w': 635, 'h': 145}, 'd': 'M 155 645 L 735 645 L 735 770', 'width': 105, 'duration': 0.5})
                    strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 2획 (중간 가로)',
                                    'clip_box': {'x': 150, 'y': 745, 'w': 635, 'h': 70}, 'd': 'M 155 775 L 780 775', 'width': 95, 'duration': 0.4})
                    strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 3획 (하단 ㄴ 꺾음)',
                                    'clip_box': {'x': 150, 'y': 795, 'w': 650, 'h': 165}, 'd': 'M 200 795 L 200 920 L 800 920', 'width': 110, 'duration': 0.65})

            # --- ㄺ ---
            elif jong == 'ㄺ':
                w_l = int(w_tot * 0.52)
                x_g = x_l + int(w_tot * 0.54)
                w_g = x_r - x_g
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 1획',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': w_l, 'h': int(h_tot*0.45)},
                                'd': f'M {x_l + 10} {y_t + 35} L {x_l + w_l - 15} {y_t + 35} L {x_l + w_l - 15} {y_t + int(h_tot*0.45)}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 2획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.35), 'w': w_l, 'h': int(h_tot*0.3)},
                                'd': f'M {x_l + 10} {y_t + int(h_tot*0.5)} L {x_l + w_l - 10} {y_t + int(h_tot*0.5)}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 3획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.45), 'w': w_l + 10, 'h': int(h_tot*0.55)},
                                'd': f'M {x_l + 35} {y_t + int(h_tot*0.5)} L {x_l + 35} {y_b - 25} L {x_l + w_l} {y_b - 25}', 'width': 105, 'duration': 0.5})
                strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㄱ 받침',
                                'clip_box': {'x': x_g - 10, 'y': y_t, 'w': w_g + 20, 'h': h_tot + 15},
                                'd': f'M {x_g} {y_t + 40} L {x_r - 10} {y_t + 40} L {x_r - 10} {y_b}', 'width': 105, 'duration': 0.5})

            # --- ㄻ ---
            elif jong == 'ㄻ':
                w_l = int(w_tot * 0.48)
                x_m = x_l + int(w_tot * 0.52)
                w_m = x_r - x_m
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 1획',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': w_l, 'h': int(h_tot*0.45)},
                                'd': f'M {x_l + 10} {y_t + 35} L {x_l + w_l - 15} {y_t + 35} L {x_l + w_l - 15} {y_t + int(h_tot*0.45)}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 2획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.35), 'w': w_l, 'h': int(h_tot*0.3)},
                                'd': f'M {x_l + 10} {y_t + int(h_tot*0.5)} L {x_l + w_l - 10} {y_t + int(h_tot*0.5)}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 3획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.45), 'w': w_l + 10, 'h': int(h_tot*0.55)},
                                'd': f'M {x_l + 35} {y_t + int(h_tot*0.5)} L {x_l + 35} {y_b - 25} L {x_l + w_l} {y_b - 25}', 'width': 105, 'duration': 0.5})
                strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅁ 1획 (좌세로)',
                                'clip_box': {'x': x_m - 10, 'y': y_t, 'w': 75, 'h': h_tot + 15}, 'd': f'M {x_m + 25} {y_t + 10} L {x_m + 25} {y_b - 15}', 'width': 100, 'duration': 0.35})
                strokes.append({'rel_order': 5, 'part': '종성', 'color': '#10b981', 'name': 'ㅁ 2획 (상우 꺾음)',
                                'clip_box': {'x': x_m + 15, 'y': y_t, 'w': w_m - 10, 'h': h_tot + 15}, 'd': f'M {x_m + 25} {y_t + 35} L {x_r - 10} {y_t + 35} L {x_r - 10} {y_b - 15}', 'width': 100, 'duration': 0.45})
                strokes.append({'rel_order': 6, 'part': '종성', 'color': '#10b981', 'name': 'ㅁ 3획 (하단 가로)',
                                'clip_box': {'x': x_m + 15, 'y': y_b - 65, 'w': w_m - 10, 'h': 65}, 'd': f'M {x_m + 25} {y_b - 25} L {x_r - 10} {y_b - 25}', 'width': 95, 'duration': 0.28})

            # --- ㄼ ---
            elif jong == 'ㄼ':
                w_l = int(w_tot * 0.48)
                x_b = x_l + int(w_tot * 0.52)
                w_b = x_r - x_b
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 1획',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': w_l, 'h': int(h_tot*0.45)},
                                'd': f'M {x_l + 10} {y_t + 35} L {x_l + w_l - 15} {y_t + 35} L {x_l + w_l - 15} {y_t + int(h_tot*0.45)}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 2획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.35), 'w': w_l, 'h': int(h_tot*0.3)},
                                'd': f'M {x_l + 10} {y_t + int(h_tot*0.5)} L {x_l + w_l - 10} {y_t + int(h_tot*0.5)}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 3획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.45), 'w': w_l + 10, 'h': int(h_tot*0.55)},
                                'd': f'M {x_l + 35} {y_t + int(h_tot*0.5)} L {x_l + 35} {y_b - 25} L {x_l + w_l} {y_b - 25}', 'width': 105, 'duration': 0.5})
                strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 1획 (좌세로)',
                                'clip_box': {'x': x_b - 10, 'y': y_t, 'w': 65, 'h': h_tot + 15}, 'd': f'M {x_b + 20} {y_t + 10} L {x_b + 20} {y_b - 15}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 5, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 2획 (우세로)',
                                'clip_box': {'x': x_r - 55, 'y': y_t, 'w': 65, 'h': h_tot + 15}, 'd': f'M {x_r - 15} {y_t + 10} L {x_r - 15} {y_b - 15}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 6, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 3획 (중가로)',
                                'clip_box': {'x': x_b + 10, 'y': y_t + int(h_tot*0.4) - 25, 'w': w_b - 20, 'h': 55}, 'd': f'M {x_b + 20} {y_t + int(h_tot*0.4)} L {x_r - 15} {y_t + int(h_tot*0.4)}', 'width': 90, 'duration': 0.25})
                strokes.append({'rel_order': 7, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 4획 (하가로)',
                                'clip_box': {'x': x_b + 10, 'y': y_b - 65, 'w': w_b - 20, 'h': 65}, 'd': f'M {x_b + 20} {y_b - 25} L {x_r - 15} {y_b - 25}', 'width': 95, 'duration': 0.25})

            # --- ㄽ ---
            elif jong == 'ㄽ':
                w_l = int(w_tot * 0.5)
                x_s = x_l + int(w_tot * 0.52)
                w_s = x_r - x_s
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 1획',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': w_l, 'h': int(h_tot*0.45)},
                                'd': f'M {x_l + 10} {y_t + 35} L {x_l + w_l - 15} {y_t + 35} L {x_l + w_l - 15} {y_t + int(h_tot*0.45)}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 2획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.35), 'w': w_l, 'h': int(h_tot*0.3)},
                                'd': f'M {x_l + 10} {y_t + int(h_tot*0.5)} L {x_l + w_l - 10} {y_t + int(h_tot*0.5)}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 3획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.45), 'w': w_l + 10, 'h': int(h_tot*0.55)},
                                'd': f'M {x_l + 35} {y_t + int(h_tot*0.5)} L {x_l + 35} {y_b - 25} L {x_l + w_l} {y_b - 25}', 'width': 105, 'duration': 0.5})
                cx = x_s + int(w_s * 0.5)
                strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅅ 1획 (좌빗침)',
                                'clip_box': {'x': x_s - 10, 'y': y_t, 'w': cx - x_s + 15, 'h': h_tot + 15}, 'd': f'M {cx} {y_t + 35} L {x_s} {y_b}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 5, 'part': '종성', 'color': '#10b981', 'name': 'ㅅ 2획 (우빗침)',
                                'clip_box': {'x': cx - 15, 'y': y_t + int(h_tot*0.3), 'w': x_r - cx + 15, 'h': int(h_tot*0.7) + 15}, 'd': f'M {cx - 10} {y_t + int(h_tot*0.35)} L {x_r} {y_b}', 'width': 100, 'duration': 0.35})

            # --- ㄾ ---
            elif jong == 'ㄾ':
                w_l = int(w_tot * 0.48)
                x_t = x_l + int(w_tot * 0.52)
                w_t = x_r - x_t
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 1획',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': w_l, 'h': int(h_tot*0.45)},
                                'd': f'M {x_l + 10} {y_t + 35} L {x_l + w_l - 15} {y_t + 35} L {x_l + w_l - 15} {y_t + int(h_tot*0.45)}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 2획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.35), 'w': w_l, 'h': int(h_tot*0.3)},
                                'd': f'M {x_l + 10} {y_t + int(h_tot*0.5)} L {x_l + w_l - 10} {y_t + int(h_tot*0.5)}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 3획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.45), 'w': w_l + 10, 'h': int(h_tot*0.55)},
                                'd': f'M {x_l + 35} {y_t + int(h_tot*0.5)} L {x_l + 35} {y_b - 25} L {x_l + w_l} {y_b - 25}', 'width': 105, 'duration': 0.5})
                strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅌ 1획 (상가로)',
                                'clip_box': {'x': x_t, 'y': y_t, 'w': w_t, 'h': 75}, 'd': f'M {x_t} {y_t + 35} L {x_r} {y_t + 35}', 'width': 100, 'duration': 0.3})
                strokes.append({'rel_order': 5, 'part': '종성', 'color': '#10b981', 'name': 'ㅌ 2획 (중가로)',
                                'clip_box': {'x': x_t, 'y': y_t + int(h_tot*0.4) - 25, 'w': w_t, 'h': 65}, 'd': f'M {x_t} {y_t + int(h_tot*0.4)} L {x_r} {y_t + int(h_tot*0.4)}', 'width': 95, 'duration': 0.25})
                strokes.append({'rel_order': 6, 'part': '종성', 'color': '#10b981', 'name': 'ㅌ 3획 (하단 ㄴ)',
                                'clip_box': {'x': x_t, 'y': y_t + 35, 'w': w_t, 'h': h_tot - 20}, 'd': f'M {x_t + 25} {y_t + 40} L {x_t + 25} {y_b - 25} L {x_r} {y_b - 25}', 'width': 105, 'duration': 0.5})

            # --- ㄿ ---
            elif jong == 'ㄿ':
                w_l = int(w_tot * 0.48)
                x_p = x_l + int(w_tot * 0.52)
                w_p = x_r - x_p
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 1획',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': w_l, 'h': int(h_tot*0.45)},
                                'd': f'M {x_l + 10} {y_t + 35} L {x_l + w_l - 15} {y_t + 35} L {x_l + w_l - 15} {y_t + int(h_tot*0.45)}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 2획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.35), 'w': w_l, 'h': int(h_tot*0.3)},
                                'd': f'M {x_l + 10} {y_t + int(h_tot*0.5)} L {x_l + w_l - 10} {y_t + int(h_tot*0.5)}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 3획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.45), 'w': w_l + 10, 'h': int(h_tot*0.55)},
                                'd': f'M {x_l + 35} {y_t + int(h_tot*0.5)} L {x_l + 35} {y_b - 25} L {x_l + w_l} {y_b - 25}', 'width': 105, 'duration': 0.5})
                strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅍ 1획 (상가로)',
                                'clip_box': {'x': x_p, 'y': y_t, 'w': w_p, 'h': 75}, 'd': f'M {x_p} {y_t + 35} L {x_r} {y_t + 35}', 'width': 100, 'duration': 0.3})
                col = int(w_p * 0.3)
                strokes.append({'rel_order': 5, 'part': '종성', 'color': '#10b981', 'name': 'ㅍ 2획 (좌세로)',
                                'clip_box': {'x': x_p + col - 25, 'y': y_t + 25, 'w': 55, 'h': h_tot - 25}, 'd': f'M {x_p + col} {y_t + 35} L {x_p + col} {y_b - 25}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 6, 'part': '종성', 'color': '#10b981', 'name': 'ㅍ 3획 (우세로)',
                                'clip_box': {'x': x_r - col - 25, 'y': y_t + 25, 'w': 55, 'h': h_tot - 25}, 'd': f'M {x_r - col} {y_t + 35} L {x_r - col} {y_b - 25}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 7, 'part': '종성', 'color': '#10b981', 'name': 'ㅍ 4획 (하가로)',
                                'clip_box': {'x': x_p, 'y': y_b - 65, 'w': w_p, 'h': 65}, 'd': f'M {x_p} {y_b - 25} L {x_r} {y_b - 25}', 'width': 100, 'duration': 0.3})

            # --- ㅀ ---
            elif jong == 'ㅀ':
                w_l = int(w_tot * 0.48)
                x_h = x_l + int(w_tot * 0.52)
                w_h = x_r - x_h
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 1획',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': w_l, 'h': int(h_tot*0.45)},
                                'd': f'M {x_l + 10} {y_t + 35} L {x_l + w_l - 15} {y_t + 35} L {x_l + w_l - 15} {y_t + int(h_tot*0.45)}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 2획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.35), 'w': w_l, 'h': int(h_tot*0.3)},
                                'd': f'M {x_l + 10} {y_t + int(h_tot*0.5)} L {x_l + w_l - 10} {y_t + int(h_tot*0.5)}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㄹ 3획',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.45), 'w': w_l + 10, 'h': int(h_tot*0.55)},
                                'd': f'M {x_l + 35} {y_t + int(h_tot*0.5)} L {x_l + 35} {y_b - 25} L {x_l + w_l} {y_b - 25}', 'width': 105, 'duration': 0.5})
                cx = x_h + int(w_h * 0.5)
                strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅎ 1획 (꼭지)',
                                'clip_box': {'x': cx - 35, 'y': y_t, 'w': 70, 'h': 65}, 'd': f'M {cx} {y_t} L {cx} {y_t + 55}', 'width': 95, 'duration': 0.25})
                strokes.append({'rel_order': 5, 'part': '종성', 'color': '#10b981', 'name': 'ㅎ 2획 (가로)',
                                'clip_box': {'x': x_h, 'y': y_t + 50, 'w': w_h, 'h': 65}, 'd': f'M {x_h} {y_t + 75} L {x_r} {y_t + 75}', 'width': 100, 'duration': 0.35})
                r_x = int(w_h * 0.38)
                r_y = int(h_tot * 0.25)
                y_c = y_b - r_y - 15
                strokes.append({'rel_order': 6, 'part': '종성', 'color': '#10b981', 'name': 'ㅎ 3획 (원형)',
                                'clip_box': {'x': cx - r_x - 20, 'y': y_t + 105, 'w': 2*r_x + 40, 'h': 2*r_y + 30},
                                'd': f'M {cx} {y_c - r_y} A {r_x} {r_y} 0 1 0 {cx} {y_c + r_y} A {r_x} {r_y} 0 1 0 {cx} {y_c - r_y}', 'width': 105, 'duration': 0.6})

            # --- ㅁ ---
            elif jong == 'ㅁ':
                if layout == 'H2': # calibrated '꿈', '봄'
                    strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅁ 받침 1획 (좌측 세로)',
                                    'clip_box': {'x': 148, 'y': 628, 'w': 89, 'h': 321}, 'd': 'M 192 628 L 192 949', 'width': 105, 'duration': 0.45})
                    strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅁ 받침 2획 (상우 꺾음)',
                                    'clip_box': {'x': 233, 'y': 628, 'w': 536, 'h': 321}, 'd': 'M 192 661 L 724 661 L 724 949', 'width': 105, 'duration': 0.65})
                    strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅁ 받침 3획 (하단 가로)',
                                    'clip_box': {'x': 233, 'y': 874, 'w': 454, 'h': 75}, 'd': 'M 192 911 L 724 911', 'width': 95, 'duration': 0.4})
                else:
                    strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅁ 받침 1획 (좌측 세로)',
                                    'clip_box': {'x': x_l, 'y': y_t, 'w': 90, 'h': h_tot}, 'd': f'M {x_l + 42} {y_t} L {x_l + 42} {y_b}', 'width': 105, 'duration': 0.45})
                    strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅁ 받침 2획 (상우 꺾음)',
                                    'clip_box': {'x': x_l + 80, 'y': y_t, 'w': w_tot - 80, 'h': h_tot}, 'd': f'M {x_l + 42} {y_t + 35} L {x_r - 20} {y_t + 35} L {x_r - 20} {y_b}', 'width': 105, 'duration': 0.65})
                    strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅁ 받침 3획 (하단 가로)',
                                    'clip_box': {'x': x_l + 80, 'y': y_b - 65, 'w': w_tot - 110, 'h': 65}, 'd': f'M {x_l + 42} {y_b - 25} L {x_r - 20} {y_b - 25}', 'width': 95, 'duration': 0.4})

            # --- ㅂ ---
            elif jong == 'ㅂ':
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 받침 1획 (좌측 기둥)',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': 95, 'h': h_tot}, 'd': f'M {x_l + 42} {y_t} L {x_l + 42} {y_b}', 'width': 110, 'duration': 0.45})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 받침 2획 (우측 기둥)',
                                'clip_box': {'x': x_r - 95, 'y': y_t, 'w': 95, 'h': h_tot}, 'd': f'M {x_r - 42} {y_t} L {x_r - 42} {y_b}', 'width': 110, 'duration': 0.45})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 받침 3획 (중간 가로)',
                                'clip_box': {'x': x_l + 75, 'y': y_t + int(h_tot*0.4) - 30, 'w': w_tot - 150, 'h': 65}, 'd': f'M {x_l + 42} {y_t + int(h_tot*0.4)} L {x_r - 42} {y_t + int(h_tot*0.4)}', 'width': 100, 'duration': 0.35})
                strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 받침 4획 (하단 가로)',
                                'clip_box': {'x': x_l + 75, 'y': y_b - 65, 'w': w_tot - 150, 'h': 65}, 'd': f'M {x_l + 42} {y_b - 25} L {x_r - 42} {y_b - 25}', 'width': 105, 'duration': 0.35})

            # --- ㅄ ---
            elif jong == 'ㅄ':
                w_b = int(w_tot * 0.5)
                x_s = x_l + int(w_tot * 0.52)
                w_s = x_r - x_s
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 1획 (좌세로)',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': 65, 'h': h_tot}, 'd': f'M {x_l + 25} {y_t} L {x_l + 25} {y_b}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 2획 (우세로)',
                                'clip_box': {'x': x_l + w_b - 65, 'y': y_t, 'w': 65, 'h': h_tot}, 'd': f'M {x_l + w_b - 25} {y_t} L {x_l + w_b - 25} {y_b}', 'width': 95, 'duration': 0.3})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 3획 (중가로)',
                                'clip_box': {'x': x_l + 20, 'y': y_t + int(h_tot*0.4) - 25, 'w': w_b - 40, 'h': 55}, 'd': f'M {x_l + 25} {y_t + int(h_tot*0.4)} L {x_l + w_b - 25} {y_t + int(h_tot*0.4)}', 'width': 90, 'duration': 0.25})
                strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅂ 4획 (하가로)',
                                'clip_box': {'x': x_l + 20, 'y': y_b - 55, 'w': w_b - 40, 'h': 55}, 'd': f'M {x_l + 25} {y_b - 20} L {x_l + w_b - 25} {y_b - 20}', 'width': 95, 'duration': 0.25})
                cx = x_s + int(w_s * 0.5)
                strokes.append({'rel_order': 5, 'part': '종성', 'color': '#10b981', 'name': 'ㅅ 1획 (좌빗침)',
                                'clip_box': {'x': x_s - 10, 'y': y_t, 'w': cx - x_s + 15, 'h': h_tot}, 'd': f'M {cx} {y_t + 35} L {x_s} {y_b}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 6, 'part': '종성', 'color': '#10b981', 'name': 'ㅅ 2획 (우빗침)',
                                'clip_box': {'x': cx - 15, 'y': y_t + int(h_tot*0.3), 'w': x_r - cx + 15, 'h': int(h_tot*0.7)}, 'd': f'M {cx - 10} {y_t + int(h_tot*0.35)} L {x_r} {y_b}', 'width': 100, 'duration': 0.35})

            # --- ㅅ ---
            elif jong == 'ㅅ':
                cx = x_l + int(w_tot * 0.5)
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅅ 받침 1획 (좌측 빗침)',
                                'clip_box': {'x': x_l - 15, 'y': y_t, 'w': cx - x_l + 20, 'h': h_tot},
                                'd': f'M {cx} {y_t + 30} C {cx} {y_t + int(h_tot*0.5)} {x_l + 40} {y_t + int(h_tot*0.8)} {x_l} {y_b}', 'width': 115, 'duration': 0.55})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅅ 받침 2획 (우측 빗침)',
                                'clip_box': {'x': cx - 20, 'y': y_t + int(h_tot*0.25), 'w': x_r - cx + 25, 'h': int(h_tot*0.75)},
                                'd': f'M {cx - 15} {y_t + int(h_tot*0.35)} L {x_r} {y_b}', 'width': 115, 'duration': 0.5})

            # --- ㅆ ---
            elif jong == 'ㅆ':
                w_half = int(w_tot * 0.48)
                gap = int(w_tot * 0.52)
                for i, prefix in enumerate(['첫째 ㅅ 받침', '둘째 ㅅ 받침']):
                    off = i * gap
                    cx = x_l + off + int(w_half * 0.55)
                    strokes.append({'rel_order': 2*i + 1, 'part': '종성', 'color': '#10b981', 'name': f'{prefix} 1획',
                                    'clip_box': {'x': x_l + off - 15, 'y': y_t, 'w': int(w_half*0.65), 'h': h_tot},
                                    'd': f'M {cx} {y_t + 30} C {cx} {y_t + int(h_tot*0.5)} {x_l + off + 30} {y_t + int(h_tot*0.8)} {x_l + off} {y_b}', 'width': 105, 'duration': 0.45})
                    strokes.append({'rel_order': 2*i + 2, 'part': '종성', 'color': '#10b981', 'name': f'{prefix} 2획',
                                    'clip_box': {'x': cx - 20, 'y': y_t + int(h_tot*0.25), 'w': int(w_half*0.6), 'h': int(h_tot*0.75)},
                                    'd': f'M {cx - 10} {y_t + int(h_tot*0.35)} L {x_l + off + w_half} {y_b}', 'width': 105, 'duration': 0.4})

            # --- ㅇ ---
            elif jong == 'ㅇ':
                if layout == 'M2': # calibrated '광', '꿩'
                    strokes.append({
                        'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅇ 받침 (원형 폐곡선)',
                        'clip_box': {'x': 150, 'y': 620, 'w': 625, 'h': 345},
                        'd': 'M 462 661 A 235 130 0 1 0 462 921 A 235 130 0 1 0 462 661', 'width': 125, 'duration': 0.8
                    })
                else:
                    cx = x_l + int(w_tot * 0.5)
                    r_x = int(w_tot * 0.42)
                    r_y = int(h_tot * 0.38)
                    y_c = y_t + int(h_tot * 0.5)
                    strokes.append({
                        'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅇ 받침 (원형 폐곡선)',
                        'clip_box': {'x': cx - r_x - 30, 'y': y_t - 15, 'w': 2*r_x + 60, 'h': h_tot + 30},
                        'd': f'M {cx} {y_c - r_y} A {r_x} {r_y} 0 1 0 {cx} {y_c + r_y} A {r_x} {r_y} 0 1 0 {cx} {y_c - r_y}', 'width': 120, 'duration': 0.8
                    })

            # --- ㅈ ---
            elif jong == 'ㅈ':
                cx = x_l + int(w_tot * 0.5)
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅈ 받침 1획 (가로-좌빗침)',
                                'clip_box': {'x': x_l - 10, 'y': y_t, 'w': w_tot + 20, 'h': h_tot},
                                'd': f'M {x_l} {y_t + 35} L {x_r} {y_t + 35} L {cx} {y_t + int(h_tot*0.35)} L {x_l} {y_b}', 'width': 110, 'duration': 0.6})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅈ 받침 2획 (우측 빗침)',
                                'clip_box': {'x': cx - 20, 'y': y_t + int(h_tot*0.25), 'w': x_r - cx + 25, 'h': int(h_tot*0.75)},
                                'd': f'M {cx} {y_t + int(h_tot*0.35)} L {x_r} {y_b}', 'width': 110, 'duration': 0.5})

            # --- ㅊ ---
            elif jong == 'ㅊ':
                if layout == 'H2': # calibrated '꽃'
                    strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅊ 1획 (상단 꼭지)',
                                    'clip_box': {'x': 410, 'y': 541, 'w': 95, 'h': 92}, 'd': 'M 457 541 L 457 633', 'width': 95, 'duration': 0.28})
                    strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅊ 2획 (가로선)',
                                    'clip_box': {'x': 145, 'y': 633, 'w': 625, 'h': 72}, 'd': 'M 145 665 L 770 665', 'width': 95, 'duration': 0.45})
                    strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅊ 3획 (좌측 빗침)',
                                    'clip_box': {'x': 110, 'y': 690, 'w': 355, 'h': 275}, 'd': 'M 465 690 C 400 780 270 860 125 935', 'width': 180, 'duration': 0.55})
                    strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅊ 4획 (우측 빗침)',
                                    'clip_box': {'x': 450, 'y': 690, 'w': 360, 'h': 275}, 'd': 'M 450 690 C 515 780 645 860 790 935', 'width': 180, 'duration': 0.55})
                else:
                    cx = x_l + int(w_tot * 0.5)
                    strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅊ 1획 (상단 꼭지)',
                                    'clip_box': {'x': cx - 45, 'y': y_t, 'w': 90, 'h': 85}, 'd': f'M {cx} {y_t} L {cx} {y_t + 75}', 'width': 95, 'duration': 0.28})
                    strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅊ 2획 (가로선)',
                                    'clip_box': {'x': x_l, 'y': y_t + 65, 'w': w_tot, 'h': 70}, 'd': f'M {x_l + 10} {y_t + 95} L {x_r - 10} {y_t + 95}', 'width': 100, 'duration': 0.4})
                    strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅊ 3획 (좌측 빗침)',
                                    'clip_box': {'x': x_l - 15, 'y': y_t + 95, 'w': cx - x_l + 20, 'h': h_tot - 95},
                                    'd': f'M {cx} {y_t + 95} L {x_l} {y_b}', 'width': 115, 'duration': 0.55})
                    strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅊ 4획 (우측 빗침)',
                                    'clip_box': {'x': cx - 20, 'y': y_t + 95, 'w': x_r - cx + 25, 'h': h_tot - 95},
                                    'd': f'M {cx} {y_t + 95} L {x_r} {y_b}', 'width': 115, 'duration': 0.5})

            # --- ㅋ ---
            elif jong == 'ㅋ':
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅋ 1획 (ㄱ 꺾음)',
                                'clip_box': {'x': x_l - 10, 'y': y_t, 'w': w_tot + 20, 'h': h_tot + 15},
                                'd': f'M {x_l} {y_t + 40} L {x_r - 10} {y_t + 40} L {x_r - 10} {y_b}', 'width': 115, 'duration': 0.6})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅋ 2획 (중간 가로)',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.45) - 30, 'w': w_tot, 'h': 65},
                                'd': f'M {x_l} {y_t + int(h_tot*0.45)} L {x_r - 20} {y_t + int(h_tot*0.45)}', 'width': 105, 'duration': 0.35})

            # --- ㅌ ---
            elif jong == 'ㅌ':
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅌ 1획 (상단 가로)',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': w_tot, 'h': 75}, 'd': f'M {x_l + 10} {y_t + 35} L {x_r - 10} {y_t + 35}', 'width': 105, 'duration': 0.35})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅌ 2획 (중간 가로)',
                                'clip_box': {'x': x_l, 'y': y_t + int(h_tot*0.45) - 25, 'w': w_tot, 'h': 65}, 'd': f'M {x_l + 10} {y_t + int(h_tot*0.45)} L {x_r - 10} {y_t + int(h_tot*0.45)}', 'width': 100, 'duration': 0.35})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅌ 3획 (하단 ㄴ 꺾음)',
                                'clip_box': {'x': x_l, 'y': y_t + 35, 'w': w_tot, 'h': h_tot - 20},
                                'd': f'M {x_l + 40} {y_t + 40} L {x_l + 40} {y_b - 25} L {x_r} {y_b - 25}', 'width': 115, 'duration': 0.6})

            # --- ㅍ ---
            elif jong == 'ㅍ':
                col = int(w_tot * 0.28)
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅍ 1획 (상단 가로)',
                                'clip_box': {'x': x_l, 'y': y_t, 'w': w_tot, 'h': 75}, 'd': f'M {x_l + 10} {y_t + 35} L {x_r - 10} {y_t + 35}', 'width': 105, 'duration': 0.35})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅍ 2획 (좌측 세로)',
                                'clip_box': {'x': x_l + col - 35, 'y': y_t + 25, 'w': 70, 'h': h_tot - 25}, 'd': f'M {x_l + col} {y_t + 35} L {x_l + col} {y_b - 25}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅍ 3획 (우측 세로)',
                                'clip_box': {'x': x_r - col - 35, 'y': y_t + 25, 'w': 70, 'h': h_tot - 25}, 'd': f'M {x_r - col} {y_t + 35} L {x_r - col} {y_b - 25}', 'width': 100, 'duration': 0.4})
                strokes.append({'rel_order': 4, 'part': '종성', 'color': '#10b981', 'name': 'ㅍ 4획 (하단 가로)',
                                'clip_box': {'x': x_l, 'y': y_b - 65, 'w': w_tot, 'h': 65}, 'd': f'M {x_l + 10} {y_b - 25} L {x_r - 10} {y_b - 25}', 'width': 105, 'duration': 0.35})

            # --- ㅎ ---
            elif jong == 'ㅎ':
                cx = x_l + int(w_tot * 0.5)
                strokes.append({'rel_order': 1, 'part': '종성', 'color': '#10b981', 'name': 'ㅎ 1획 (꼭지)',
                                'clip_box': {'x': cx - 40, 'y': y_t, 'w': 80, 'h': 75}, 'd': f'M {cx} {y_t} L {cx} {y_t + 65}', 'width': 95, 'duration': 0.28})
                strokes.append({'rel_order': 2, 'part': '종성', 'color': '#10b981', 'name': 'ㅎ 2획 (가로선)',
                                'clip_box': {'x': x_l, 'y': y_t + 55, 'w': w_tot, 'h': 75}, 'd': f'M {x_l + 10} {y_t + 85} L {x_r - 10} {y_t + 85}', 'width': 105, 'duration': 0.38})
                r_x = int(w_tot * 0.38)
                r_y = int(h_tot * 0.26)
                y_c = y_b - r_y - 15
                strokes.append({'rel_order': 3, 'part': '종성', 'color': '#10b981', 'name': 'ㅎ 3획 (원형 폐곡선)',
                                'clip_box': {'x': cx - r_x - 25, 'y': y_t + 120, 'w': 2*r_x + 50, 'h': 2*r_y + 35},
                                'd': f'M {cx} {y_c - r_y} A {r_x} {r_y} 0 1 0 {cx} {y_c + r_y} A {r_x} {r_y} 0 1 0 {cx} {y_c - r_y}', 'width': 110, 'duration': 0.7})

            # Total bounding box
            min_x = min(s['clip_box']['x'] for s in strokes)
            min_y = min(s['clip_box']['y'] for s in strokes)
            max_x = max(s['clip_box']['x'] + s['clip_box']['w'] for s in strokes)
            max_y = max(s['clip_box']['y'] + s['clip_box']['h'] for s in strokes)

            modules[jong][layout] = {
                'jamo': jong,
                'part': '종성',
                'layout': layout,
                'layout_desc': JONG_LAYOUT_DESCRIPTIONS[layout],
                'stroke_count': len(strokes),
                'bbox': {'x': min_x, 'y': min_y, 'w': max_x - min_x, 'h': max_y - min_y},
                'strokes': strokes
            }

    return modules


def build_master_jamo_library():
    print("Building Calibrated Master Jamo Modular Library (258 components)...")

    cho_mods = generate_cho_modules()
    jung_mods = generate_jung_modules()
    jong_mods = generate_jong_modules()

    cho_count = sum(len(v) for v in cho_mods.values())
    jung_count = sum(len(v) for v in jung_mods.values())
    jong_count = sum(len(v) for v in jong_mods.values())
    grand_total = cho_count + jung_count + jong_count

    print(f"  [1/3] Cho modules:  19 x 6 = {cho_count} parts (expected 114)")
    print(f"  [2/3] Jung modules: 21 x 3 = {jung_count} parts (expected 63)")
    print(f"  [3/3] Jong modules: 27 x 3 = {jong_count} parts (expected 81)")
    print(f"  Total Standard Components: {grand_total} parts (expected 258)")

    assert cho_count == 114
    assert jung_count == 63
    assert jong_count == 81
    assert grand_total == 258

    master_library = {
        'metadata': {
            'title': 'Noto Sans KR Master Jamo Modular Library (258 Canonical Parts)',
            'version': '1.0.0',
            'font': 'Noto Sans CJK KR Regular',
            'created_at': '2026-11-10',
            'standards': '0px Bleeding / 100% Coverage / Korean Stroke Order',
            'total_components': grand_total,
            'breakdown': {
                'cho_components': cho_count,
                'jung_components': jung_count,
                'jong_components': jong_count
            },
            'layouts': ['V1', 'V2', 'H1', 'H2', 'M1', 'M2'],
            'layout_descriptions': LAYOUT_DESCRIPTIONS,
            'beol_descriptions': BEOL_DESCRIPTIONS,
            'jong_layout_descriptions': JONG_LAYOUT_DESCRIPTIONS
        },
        'cho_modules': cho_mods,
        'jung_modules': jung_mods,
        'jong_modules': jong_mods
    }

    out_file = '/home/antigravity/parkjinsoo8485/machine_learning/hangul_stroke_engine/master_jamo_library.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(master_library, f, ensure_ascii=False, indent=2)

    print(f"\nSuccessfully generated master library at: {out_file}")
    file_size_kb = os.path.getsize(out_file) / 1024
    print(f"Library file size: {file_size_kb:.1f} KB")

if __name__ == '__main__':
    build_master_jamo_library()
