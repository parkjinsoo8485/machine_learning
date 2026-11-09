"""
Jamo Rules Library for Noto Sans CJK KR - Fully Calibrated Edition
===================================================================
Defines canonical stroke orders, overshoot trajectories, and bounding box offsets
for all 19 Initial Consonants (Cho), 21 Vowels (Jung), and 27 Final Consonants (Jong)
across all structural layout archetypes (V1, V2, H1, H2, C1, C2).
"""

from typing import Dict, List, Any

CHO_LIST = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
JUNG_LIST = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
JONG_LIST = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

def get_cho_strokes(cho: str, archetype: str, start_order: int, jung: str = '') -> List[Dict[str, Any]]:
    strokes = []
    ord_num = start_order

    is_vert = archetype in ('V1', 'V2', 'C1', 'C2')
    has_jong = archetype in ('V2', 'H2', 'C2')

    if archetype == 'V1':
        y_top, y_bot, w_right = 140, 720, (510 if jung in ('ㅐ', 'ㅔ', 'ㅒ', 'ㅖ') else 580)
    elif archetype == 'V2':
        y_top, y_bot, w_right = 100, 580, (510 if jung in ('ㅐ', 'ㅔ', 'ㅒ', 'ㅖ') else 570)
    elif archetype == 'H1':
        if jung in ('ㅜ', 'ㅠ'):
            y_top, y_bot, w_right = 100, 480, 780
        elif jung == 'ㅡ':
            y_top, y_bot, w_right = 110, 700, 800
        else: # ㅗ, ㅛ
            y_top, y_bot, w_right = 110, 550, 800
    elif archetype == 'H2':
        y_top, y_bot, w_right = 80, 440, 780
    elif archetype == 'C1':
        y_top, y_bot, w_right = 110, 550, 540
    else: # C2
        y_top, y_bot, w_right = 90, 400, 540

    # --- ㄱ ---
    if cho == 'ㄱ':
        if archetype == 'V1':
            if jung in ('ㅐ', 'ㅔ', 'ㅒ', 'ㅖ'):
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (곡선 꺾음)',
                    'clip_box': {'x': 40, 'y': 140, 'w': 420, 'h': 650},
                    'd': 'M 80 185 L 430 185 C 410 380 320 620 55 755', 'width': 110, 'duration': 0.65
                })
            else:
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (곡선 꺾음)',
                    'clip_box': {'x': 50, 'y': 140, 'w': 470, 'h': 650},
                    'd': 'M 90 185 L 485 185 C 470 400 360 620 55 755', 'width': 105, 'duration': 0.65
                })
        elif archetype == 'V2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (곡선 꺾음)',
                'clip_box': {'x': 40, 'y': 90, 'w': 490, 'h': 510},
                'd': 'M 80 140 L 485 140 C 485 340 340 520 55 580', 'width': 120, 'duration': 0.6
            })
        elif archetype == 'C1':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (상단 꺾음)',
                'clip_box': {'x': 80, 'y': 140, 'w': 480, 'h': 430},
                'd': 'M 91 186 L 506 186 L 480 565', 'width': 105, 'duration': 0.6
            })
        elif archetype == 'C2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (상단 꺾음)',
                'clip_box': {'x': 80, 'y': 90, 'w': 480, 'h': 340},
                'd': 'M 99 135 L 506 135 L 482 420', 'width': 110, 'duration': 0.55
            })
        elif archetype == 'H1':
            if jung in ('ㅜ', 'ㅠ'):
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (직각 꺾음)',
                    'clip_box': {'x': 120, 'y': 100, 'w': 670, 'h': 400},
                    'd': 'M 130 155 L 725 155 C 725 250 725 350 690 480', 'width': 120, 'duration': 0.6
                })
            else:
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (직각 꺾음)',
                    'clip_box': {'x': 120, 'y': 130, 'w': 670, 'h': 580},
                    'd': 'M 130 185 L 725 185 C 725 340 725 500 690 670', 'width': 120, 'duration': 0.6
                })
        else: # H2
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (직각 꺾음)',
                'clip_box': {'x': 135, 'y': 80, 'w': 635, 'h': 380},
                'd': 'M 140 135 L 735 135 C 735 240 735 340 695 440', 'width': 115, 'duration': 0.6
            })

    # --- ㄲ ---
    elif cho == 'ㄲ':
        if not is_vert:
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㄱ',
                'clip_box': {'x': 110, 'y': 80, 'w': 295, 'h': 325},
                'd': 'M 115 122 L 365 122 C 375 220 360 320 310 395', 'width': 125, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㄱ',
                'clip_box': {'x': 460, 'y': 80, 'w': 325, 'h': 325},
                'd': 'M 460 122 L 745 122 C 755 220 740 320 690 395', 'width': 125, 'duration': 0.45
            })
        else:
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㄱ',
                'clip_box': {'x': 50, 'y': y_top - 10, 'w': 250, 'h': y_bot - y_top + 30},
                'd': f'M 60 {y_top + 35} L 280 {y_top + 35} L 240 {y_bot}', 'width': 105, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㄱ',
                'clip_box': {'x': 295, 'y': y_top - 10, 'w': 260, 'h': y_bot - y_top + 30},
                'd': f'M 310 {y_top + 35} L 540 {y_top + 35} L 500 {y_bot}', 'width': 105, 'duration': 0.45
            })

    # --- ㄴ ---
    elif cho == 'ㄴ':
        if archetype == 'V1':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (세로-가로 꺾음)',
                'clip_box': {'x': 75, 'y': 130, 'w': 515, 'h': 615},
                'd': 'M 135 140 L 135 690 L 580 690', 'width': 115, 'duration': 0.65
            })
        elif archetype == 'V2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (세로-가로 꺾음)',
                'clip_box': {'x': 75, 'y': 90, 'w': 515, 'h': 510},
                'd': 'M 135 100 L 135 580 L 580 580', 'width': 120, 'duration': 0.6
            })
        elif archetype == 'H1':
            y_b_n = 440 if jung in ('ㅜ', 'ㅠ') else 510
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (세로-가로 꺾음)',
                'clip_box': {'x': 140, 'y': 80, 'w': 660, 'h': y_b_n - 40},
                'd': f'M 195 80 L 195 {y_b_n} L 785 {y_b_n}', 'width': 115, 'duration': 0.65
            })
        elif archetype == 'H2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (세로-가로 꺾음)',
                'clip_box': {'x': 140, 'y': 80, 'w': 660, 'h': 330},
                'd': 'M 195 80 L 195 370 L 785 370', 'width': 120, 'duration': 0.65
            })
        else: # C1, C2
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (세로-가로 꺾음)',
                'clip_box': {'x': 75, 'y': y_top - 10, 'w': 480, 'h': y_bot - y_top + 40},
                'd': f'M 135 {y_top} L 135 {y_bot} L 530 {y_bot}', 'width': 110, 'duration': 0.6
            })

    # --- ㄷ ---
    elif cho == 'ㄷ':
        if archetype == 'V1':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                'clip_box': {'x': 70, 'y': 120, 'w': 520, 'h': 110},
                'd': 'M 80 180 L 580 180', 'width': 110, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                'clip_box': {'x': 70, 'y': 175, 'w': 520, 'h': 570},
                'd': 'M 140 175 L 140 690 L 580 690', 'width': 115, 'duration': 0.6
            })
        elif archetype == 'V2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                'clip_box': {'x': 80, 'y': 90, 'w': 510, 'h': 95},
                'd': 'M 90 140 L 575 140', 'width': 120, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                'clip_box': {'x': 80, 'y': 135, 'w': 510, 'h': 450},
                'd': 'M 145 135 L 145 560 L 575 560', 'width': 120, 'duration': 0.6
            })
        elif archetype == 'H1':
            if jung in ('ㅜ', 'ㅠ'):
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                    'clip_box': {'x': 140, 'y': 90, 'w': 660, 'h': 110},
                    'd': 'M 150 140 L 780 140', 'width': 110, 'duration': 0.4
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                    'clip_box': {'x': 140, 'y': 130, 'w': 660, 'h': 350},
                    'd': 'M 195 130 L 195 430 L 780 430', 'width': 115, 'duration': 0.6
                })
            else:
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                    'clip_box': {'x': 140, 'y': 100, 'w': 660, 'h': 130},
                    'd': 'M 150 160 L 780 160', 'width': 110, 'duration': 0.4
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                    'clip_box': {'x': 140, 'y': 150, 'w': 660, 'h': 400},
                    'd': 'M 195 150 L 195 510 L 780 510', 'width': 115, 'duration': 0.6
                })
        elif archetype == 'H2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                'clip_box': {'x': 140, 'y': 80, 'w': 660, 'h': 105},
                'd': 'M 150 140 L 780 140', 'width': 110, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                'clip_box': {'x': 140, 'y': 135, 'w': 660, 'h': 290},
                'd': 'M 195 135 L 195 380 L 780 380', 'width': 115, 'duration': 0.6
            })
        else:
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                'clip_box': {'x': 70, 'y': y_top - 15, 'w': 480, 'h': 95},
                'd': f'M 80 {y_top + 30} L 520 {y_top + 30}', 'width': 105, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                'clip_box': {'x': 70, 'y': y_top + 25, 'w': 480, 'h': y_bot - y_top + 10},
                'd': f'M 135 {y_top + 25} L 135 {y_bot} L 520 {y_bot}', 'width': 110, 'duration': 0.55
            })

    # --- ㄸ ---
    elif cho == 'ㄸ':
        w_half = 250 if is_vert else 340
        x_gap = 270 if is_vert else 370
        strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㄷ 1획',
                        'clip_box': {'x': 50, 'y': y_top - 20, 'w': w_half, 'h': 90},
                        'd': f'M 60 {y_top} L {w_half + 40} {y_top}', 'width': 90, 'duration': 0.35})
        strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㄷ 2획',
                        'clip_box': {'x': 50, 'y': y_top + 30, 'w': w_half, 'h': y_bot - y_top + 30},
                        'd': f'M 90 {y_top + 20} L 90 {y_bot} L {w_half + 40} {y_bot}', 'width': 95, 'duration': 0.5})
        strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㄷ 1획',
                        'clip_box': {'x': x_gap, 'y': y_top - 20, 'w': w_half, 'h': 90},
                        'd': f'M {x_gap + 10} {y_top} L {x_gap + w_half - 10} {y_top}', 'width': 90, 'duration': 0.35})
        strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㄷ 2획',
                        'clip_box': {'x': x_gap, 'y': y_top + 30, 'w': w_half, 'h': y_bot - y_top + 30},
                        'd': f'M {x_gap + 40} {y_top + 20} L {x_gap + 40} {y_bot} L {x_gap + w_half - 10} {y_bot}', 'width': 95, 'duration': 0.5})

    # --- ㄹ ---
    elif cho == 'ㄹ':
        if archetype == 'V1':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 1획 (상단 ㄱ)',
                'clip_box': {'x': 70, 'y': 110, 'w': 520, 'h': 210},
                'd': 'M 80 160 L 580 160 L 580 290', 'width': 110, 'duration': 0.5
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 2획 (중간 가로)',
                'clip_box': {'x': 70, 'y': 280, 'w': 520, 'h': 130},
                'd': 'M 140 330 L 580 330', 'width': 110, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 3획 (하단 ㄴ)',
                'clip_box': {'x': 70, 'y': 380, 'w': 520, 'h': 360},
                'd': 'M 140 380 L 140 690 L 580 690', 'width': 115, 'duration': 0.6
            })
        elif archetype == 'V2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 1획 (상단 ㄱ)',
                'clip_box': {'x': 70, 'y': 80, 'w': 520, 'h': 170},
                'd': 'M 80 130 L 575 130 L 575 240', 'width': 110, 'duration': 0.5
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 2획 (중간 가로)',
                'clip_box': {'x': 70, 'y': 210, 'w': 520, 'h': 110},
                'd': 'M 140 250 L 575 250', 'width': 110, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 3획 (하단 ㄴ)',
                'clip_box': {'x': 70, 'y': 280, 'w': 520, 'h': 320},
                'd': 'M 140 280 L 140 550 L 580 550', 'width': 115, 'duration': 0.55
            })
        elif archetype == 'H1':
            if jung in ('ㅜ', 'ㅠ'):
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 1획 (상단 ㄱ)',
                    'clip_box': {'x': 120, 'y': 80, 'w': 670, 'h': 130},
                    'd': 'M 130 130 L 780 130 L 740 260', 'width': 110, 'duration': 0.5
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 2획 (중간 가로)',
                    'clip_box': {'x': 120, 'y': 210, 'w': 670, 'h': 130},
                    'd': 'M 140 270 L 780 270', 'width': 110, 'duration': 0.4
                })
                strokes.append({
                    'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 3획 (하단 ㄴ)',
                    'clip_box': {'x': 120, 'y': 260, 'w': 670, 'h': 240},
                    'd': 'M 180 260 L 180 480 L 780 480', 'width': 115, 'duration': 0.55
                })
            else:
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 1획 (상단 ㄱ)',
                    'clip_box': {'x': 140, 'y': 100, 'w': 660, 'h': 240},
                    'd': 'M 150 155 L 727 155 L 727 350', 'width': 110, 'duration': 0.5
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 2획 (중간 가로)',
                    'clip_box': {'x': 140, 'y': 310, 'w': 660, 'h': 90},
                    'd': 'M 190 350 L 727 350', 'width': 105, 'duration': 0.4
                })
                strokes.append({
                    'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 3획 (하단 ㄴ)',
                    'clip_box': {'x': 140, 'y': 350, 'w': 660, 'h': 250},
                    'd': 'M 195 350 L 195 574 L 727 574', 'width': 115, 'duration': 0.6
                })
        else: # H2, C1, C2
            y1 = y_top + int((y_bot - y_top) * 0.35)
            y2 = y_top + int((y_bot - y_top) * 0.65)
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 1획 (상단 ㄱ)',
                            'clip_box': {'x': 80, 'y': y_top - 15, 'w': w_right - 60, 'h': y1 - y_top + 30},
                            'd': f'M 90 {y_top + 30} L {w_right} {y_top + 30} L {w_right} {y1}', 'width': 100, 'duration': 0.5})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 2획 (중간 가로)',
                            'clip_box': {'x': 80, 'y': y1 - 10, 'w': w_right - 60, 'h': y2 - y1 + 20},
                            'd': f'M 130 {y1} L {w_right} {y1}', 'width': 100, 'duration': 0.4})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 3획 (하단 ㄴ)',
                            'clip_box': {'x': 80, 'y': y2 - 10, 'w': w_right - 60, 'h': y_bot - y2 + 30},
                            'd': f'M 130 {y2} L 130 {y_bot} L {w_right} {y_bot}', 'width': 105, 'duration': 0.55})

    # --- ㅁ ---
    elif cho == 'ㅁ':
        if archetype == 'H1' and jung in ('ㅜ', 'ㅠ'):
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 1획 (좌측 세로)',
                'clip_box': {'x': 130, 'y': 90, 'w': 140, 'h': 360},
                'd': 'M 190 90 L 190 430', 'width': 110, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 2획 (상단-우측 꺾음)',
                'clip_box': {'x': 180, 'y': 90, 'w': 630, 'h': 360},
                'd': 'M 180 140 L 760 140 L 760 430', 'width': 110, 'duration': 0.55
            })
            strokes.append({
                'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 3획 (하단 가로)',
                'clip_box': {'x': 180, 'y': 380, 'w': 630, 'h': 100},
                'd': 'M 180 430 L 760 430', 'width': 110, 'duration': 0.35
            })
        else:
            w_box = w_right - 100
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 1획 (좌측 세로)',
                            'clip_box': {'x': 60, 'y': y_top - 15, 'w': 130, 'h': y_bot - y_top + 30},
                            'd': f'M 120 {y_top} L 120 {y_bot}', 'width': 105, 'duration': 0.4})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 2획 (상단-우측 꺾음)',
                            'clip_box': {'x': 110, 'y': y_top - 15, 'w': w_box, 'h': y_bot - y_top + 30},
                            'd': f'M 120 {y_top + 30} L {w_right} {y_top + 30} L {w_right} {y_bot}', 'width': 105, 'duration': 0.55})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 3획 (하단 가로)',
                            'clip_box': {'x': 110, 'y': y_bot - 45, 'w': w_box, 'h': 85},
                            'd': f'M 120 {y_bot} L {w_right} {y_bot}', 'width': 105, 'duration': 0.35})

    # --- ㅂ ---
    elif cho == 'ㅂ':
        if archetype == 'V1' and jung == 'ㅏ':
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 1획 (좌측 기둥)',
                            'clip_box': {'x': 80, 'y': 120, 'w': 160, 'h': 630}, 'd': 'M 127 125 L 127 710', 'width': 115, 'duration': 0.5})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 2획 (우측 기둥)',
                            'clip_box': {'x': 400, 'y': 120, 'w': 160, 'h': 630}, 'd': 'M 466 125 L 466 710', 'width': 115, 'duration': 0.5})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 3획 (중간 가로)',
                            'clip_box': {'x': 80, 'y': 330, 'w': 480, 'h': 130}, 'd': 'M 120 395 L 475 395', 'width': 110, 'duration': 0.35})
            strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 4획 (하단 가로)',
                            'clip_box': {'x': 80, 'y': 640, 'w': 480, 'h': 120}, 'd': 'M 120 706 L 475 706', 'width': 115, 'duration': 0.35})
        elif archetype == 'H1' and jung in ('ㅜ', 'ㅠ'):
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 1획 (좌측 기둥)',
                            'clip_box': {'x': 130, 'y': 80, 'w': 140, 'h': 380}, 'd': 'M 188 80 L 188 440', 'width': 110, 'duration': 0.5})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 2획 (우측 기둥)',
                            'clip_box': {'x': 670, 'y': 80, 'w': 140, 'h': 380}, 'd': 'M 730 80 L 730 440', 'width': 110, 'duration': 0.5})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 3획 (중간 가로)',
                            'clip_box': {'x': 180, 'y': 200, 'w': 570, 'h': 100}, 'd': 'M 180 240 L 740 240', 'width': 105, 'duration': 0.35})
            strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 4획 (하단 가로)',
                            'clip_box': {'x': 180, 'y': 380, 'w': 570, 'h': 100}, 'd': 'M 180 430 L 740 430', 'width': 105, 'duration': 0.35})
        elif archetype == 'H1':
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 1획 (좌측 기둥)',
                            'clip_box': {'x': 130, 'y': 100, 'w': 140, 'h': 470}, 'd': 'M 188 100 L 188 546', 'width': 110, 'duration': 0.5})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 2획 (우측 기둥)',
                            'clip_box': {'x': 670, 'y': 100, 'w': 140, 'h': 470}, 'd': 'M 730 100 L 730 546', 'width': 110, 'duration': 0.5})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 3획 (중간 가로)',
                            'clip_box': {'x': 180, 'y': 270, 'w': 570, 'h': 90}, 'd': 'M 180 313 L 740 313', 'width': 105, 'duration': 0.35})
            strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 4획 (하단 가로)',
                            'clip_box': {'x': 180, 'y': 490, 'w': 570, 'h': 90}, 'd': 'M 180 546 L 740 546', 'width': 105, 'duration': 0.35})
        else:
            w_b = w_right - 60
            y_mid = y_top + int((y_bot - y_top) * 0.5)
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 1획 (좌측 기둥)',
                            'clip_box': {'x': 60, 'y': y_top - 15, 'w': 120, 'h': y_bot - y_top + 30},
                            'd': f'M 120 {y_top} L 120 {y_bot}', 'width': 105, 'duration': 0.5})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 2획 (우측 기둥)',
                            'clip_box': {'x': w_right - 50, 'y': y_top - 15, 'w': 120, 'h': y_bot - y_top + 30},
                            'd': f'M {w_right} {y_top} L {w_right} {y_bot}', 'width': 105, 'duration': 0.5})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 3획 (중간 가로)',
                            'clip_box': {'x': 100, 'y': y_mid - 40, 'w': w_b, 'h': 80},
                            'd': f'M 120 {y_mid} L {w_right} {y_mid}', 'width': 100, 'duration': 0.35})
            strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 4획 (하단 가로)',
                            'clip_box': {'x': 100, 'y': y_bot - 45, 'w': w_b, 'h': 85},
                            'd': f'M 120 {y_bot} L {w_right} {y_bot}', 'width': 105, 'duration': 0.35})

    # --- ㅃ ---
    elif cho == 'ㅃ':
        w_half = 200 if is_vert else 300
        x_g = 220 if is_vert else 340
        y_mid = y_top + int((y_bot - y_top) * 0.5)
        for offset, prefix in [(0, '첫째 ㅂ'), (x_g, '둘째 ㅂ')]:
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 1획',
                            'clip_box': {'x': 50 + offset, 'y': y_top - 10, 'w': 70, 'h': y_bot - y_top + 20},
                            'd': f'M {80 + offset} {y_top} L {80 + offset} {y_bot}', 'width': 85, 'duration': 0.4})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 2획',
                            'clip_box': {'x': offset + w_half - 20, 'y': y_top - 10, 'w': 70, 'h': y_bot - y_top + 20},
                            'd': f'M {offset + w_half + 10} {y_top} L {offset + w_half + 10} {y_bot}', 'width': 85, 'duration': 0.4})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 3획',
                            'clip_box': {'x': 60 + offset, 'y': y_mid - 30, 'w': w_half - 30, 'h': 60},
                            'd': f'M {80 + offset} {y_mid} L {offset + w_half + 10} {y_mid}', 'width': 85, 'duration': 0.3})
            strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': f'{prefix} 4획',
                            'clip_box': {'x': 60 + offset, 'y': y_bot - 35, 'w': w_half - 30, 'h': 70},
                            'd': f'M {80 + offset} {y_bot} L {offset + w_half + 10} {y_bot}', 'width': 85, 'duration': 0.3})
            ord_num += 4
        return strokes

    # --- ㅅ ---
    elif cho == 'ㅅ':
        if archetype == 'V1':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 1획 (좌측 빗침)',
                'clip_box': {'x': 25, 'y': 140, 'w': 350, 'h': 610},
                'd': 'M 312 145 C 312 360 200 620 40 735', 'width': 115, 'duration': 0.65
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 2획 (우측 빗침)',
                'clip_box': {'x': 280, 'y': 380, 'w': 320, 'h': 370},
                'd': 'M 312 430 L 580 735', 'width': 115, 'duration': 0.55
            })
        elif archetype == 'V2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 1획 (좌측 빗침)',
                'clip_box': {'x': 30, 'y': 90, 'w': 350, 'h': 520},
                'd': 'M 312 110 C 312 280 200 480 40 590', 'width': 120, 'duration': 0.6
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 2획 (우측 빗침)',
                'clip_box': {'x': 270, 'y': 220, 'w': 330, 'h': 390},
                'd': 'M 312 260 L 580 590', 'width': 120, 'duration': 0.55
            })
        elif archetype == 'H1':
            if jung in ('ㅜ', 'ㅠ'):
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 1획 (좌측 빗침)',
                    'clip_box': {'x': 50, 'y': 70, 'w': 460, 'h': 470},
                    'd': 'M 459 85 C 459 220 320 380 90 515', 'width': 110, 'duration': 0.6
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 2획 (우측 빗침)',
                    'clip_box': {'x': 440, 'y': 160, 'w': 420, 'h': 380},
                    'd': 'M 460 210 C 500 280 650 380 825 515', 'width': 110, 'duration': 0.55
                })
            else:
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 1획 (좌측 빗침)',
                    'clip_box': {'x': 50, 'y': 80, 'w': 460, 'h': 520},
                    'd': 'M 459 95 C 459 260 320 480 90 590', 'width': 110, 'duration': 0.6
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 2획 (우측 빗침)',
                    'clip_box': {'x': 440, 'y': 240, 'w': 420, 'h': 360},
                    'd': 'M 460 290 C 500 360 650 480 825 590', 'width': 110, 'duration': 0.55
                })
        else: # H2, C1, C2
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 1획 (좌측 빗침)',
                            'clip_box': {'x': 50, 'y': y_top - 15, 'w': 440, 'h': y_bot - y_top + 30},
                            'd': f'M 459 {y_top} C 459 {y_top + 140} 320 {y_bot - 40} 90 {y_bot}', 'width': 110, 'duration': 0.6})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 2획 (우측 빗침)',
                            'clip_box': {'x': 440, 'y': y_top + 80, 'w': w_right - 420, 'h': y_bot - y_top - 60},
                            'd': f'M 460 {y_top + 100} C 500 {y_top + 180} 650 {y_bot - 40} {w_right} {y_bot}', 'width': 110, 'duration': 0.55})

    # --- ㅆ ---
    elif cho == 'ㅆ':
        w_half = 260 if is_vert else 350
        x_gap = 260 if is_vert else 360
        strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㅅ 1획',
                        'clip_box': {'x': 40, 'y': y_top - 10, 'w': w_half, 'h': y_bot - y_top + 20},
                        'd': f'M {w_half - 30} {y_top} C {w_half - 30} {y_top + 140} 120 {y_bot - 40} 50 {y_bot}', 'width': 95, 'duration': 0.5})
        strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㅅ 2획',
                        'clip_box': {'x': w_half - 60, 'y': y_top + 60, 'w': 100, 'h': y_bot - y_top - 40},
                        'd': f'M {w_half - 30} {y_top + 90} L {w_half + 30} {y_bot}', 'width': 95, 'duration': 0.45})
        strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㅅ 1획',
                        'clip_box': {'x': x_gap + 20, 'y': y_top - 10, 'w': w_half, 'h': y_bot - y_top + 20},
                        'd': f'M {x_gap + w_half - 40} {y_top} C {x_gap + w_half - 40} {y_top + 140} {x_gap + 80} {y_bot - 40} {x_gap + 20} {y_bot}', 'width': 95, 'duration': 0.5})
        strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㅅ 2획',
                        'clip_box': {'x': x_gap + w_half - 60, 'y': y_top + 60, 'w': 110, 'h': y_bot - y_top - 40},
                        'd': f'M {x_gap + w_half - 40} {y_top + 90} L {x_gap + w_half + 40} {y_bot}', 'width': 95, 'duration': 0.45})

    # --- ㅇ ---
    elif cho == 'ㅇ':
        if archetype == 'V1':
            if jung in ('ㅐ', 'ㅔ', 'ㅒ', 'ㅖ'):
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (원형 폐곡선)',
                    'clip_box': {'x': 45, 'y': 100, 'w': 420, 'h': 680},
                    'd': 'M 245 165 A 150 265 0 1 0 245 695 A 150 265 0 1 0 245 165', 'width': 120, 'duration': 0.85
                })
            else:
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (원형 폐곡선)',
                    'clip_box': {'x': 55, 'y': 100, 'w': 510, 'h': 680},
                    'd': 'M 312.5 165.5 A 187 273 0 1 0 312.5 711.5 A 187 273 0 1 0 312.5 165.5', 'width': 120, 'duration': 0.85
                })
        elif archetype == 'V2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (원형 폐곡선)',
                'clip_box': {'x': 60, 'y': 100, 'w': 500, 'h': 480},
                'd': 'M 306 125 A 210 210 0 1 0 306 550 A 210 210 0 1 0 306 125', 'width': 120, 'duration': 0.8
            })
        elif archetype == 'H1':
            if jung in ('ㅜ', 'ㅠ'):
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (원형 폐곡선)',
                    'clip_box': {'x': 120, 'y': 80, 'w': 680, 'h': 420},
                    'd': 'M 459 90 A 240 190 0 1 0 459 470 A 240 190 0 1 0 459 90', 'width': 120, 'duration': 0.8
                })
            else:
                strokes.append({
                    'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (원형 폐곡선)',
                    'clip_box': {'x': 120, 'y': 100, 'w': 680, 'h': 470},
                    'd': 'M 459 110 A 240 210 0 1 0 459 530 A 240 210 0 1 0 459 110', 'width': 120, 'duration': 0.8
                })
        elif archetype == 'H2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (원형 폐곡선)',
                'clip_box': {'x': 120, 'y': 50, 'w': 670, 'h': 350},
                'd': 'M 458 100 A 275 125 0 1 0 458 351 A 275 125 0 1 0 458 100', 'width': 115, 'duration': 0.8
            })
        else: # C1, C2
            c_y = (y_top + y_bot) // 2
            r_y = (y_bot - y_top) // 2 - 10
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (원형 폐곡선)',
                            'clip_box': {'x': 70, 'y': y_top - 15, 'w': 480, 'h': y_bot - y_top + 30},
                            'd': f'M 312 {c_y - r_y} A 180 {r_y} 0 1 0 312 {c_y + r_y} A 180 {r_y} 0 1 0 312 {c_y - r_y}', 'width': 115, 'duration': 0.8})

    # --- ㅈ ---
    elif cho == 'ㅈ':
        if archetype == 'V1':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 1획 (가로선)',
                'clip_box': {'x': 70, 'y': 125, 'w': 530, 'h': 95},
                'd': 'M 90 185 L 575 185', 'width': 105, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 2획 (수직-곡선 빗침)',
                'clip_box': {'x': 25, 'y': 170, 'w': 350, 'h': 570},
                'd': 'M 312 185 L 312 320 C 312 520 200 660 50 720', 'width': 115, 'duration': 0.6
            })
            strokes.append({
                'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 3획 (우측 빗침)',
                'clip_box': {'x': 280, 'y': 320, 'w': 320, 'h': 420},
                'd': 'M 312 430 L 580 720', 'width': 115, 'duration': 0.55
            })
        elif archetype == 'V2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 1획 (가로선)',
                'clip_box': {'x': 70, 'y': 85, 'w': 530, 'h': 95},
                'd': 'M 90 145 L 575 145', 'width': 105, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 2획 (수직-곡선 빗침)',
                'clip_box': {'x': 25, 'y': 120, 'w': 350, 'h': 490},
                'd': 'M 312 145 L 312 280 C 312 440 200 520 50 590', 'width': 115, 'duration': 0.6
            })
            strokes.append({
                'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 3획 (우측 빗침)',
                'clip_box': {'x': 280, 'y': 220, 'w': 310, 'h': 390},
                'd': 'M 312 260 L 580 590', 'width': 115, 'duration': 0.55
            })
        elif archetype == 'H1':
            y_b_z = 500 if jung in ('ㅜ', 'ㅠ') else 540
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 1획 (가로선)',
                'clip_box': {'x': 130, 'y': 70, 'w': 660, 'h': 100},
                'd': 'M 140 120 L 780 120', 'width': 105, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 2획 (좌측 빗침)',
                'clip_box': {'x': 70, 'y': 110, 'w': 410, 'h': y_b_z - 90},
                'd': f'M 459 120 C 459 240 320 380 100 {y_b_z}', 'width': 110, 'duration': 0.55
            })
            strokes.append({
                'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 3획 (우측 빗침)',
                'clip_box': {'x': 440, 'y': 150, 'w': 410, 'h': y_b_z - 130},
                'd': f'M 460 220 C 500 280 650 380 815 {y_b_z}', 'width': 110, 'duration': 0.55
            })
        else: # H2, C1, C2
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 1획 (가로선)',
                            'clip_box': {'x': 130, 'y': 70, 'w': 660, 'h': 90}, 'd': 'M 140 120 L 780 120', 'width': 105, 'duration': 0.4})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 2획 (좌측 빗침)',
                            'clip_box': {'x': 70, 'y': 110, 'w': 410, 'h': y_bot - 90},
                            'd': f'M 459 120 C 459 240 320 380 100 {y_bot}', 'width': 110, 'duration': 0.55})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 3획 (우측 빗침)',
                            'clip_box': {'x': 440, 'y': 150, 'w': 410, 'h': y_bot - 130},
                            'd': f'M 460 220 C 500 280 650 380 815 {y_bot}', 'width': 110, 'duration': 0.55})

    # --- ㅉ ---
    elif cho == 'ㅉ':
        w_half = 260 if is_vert else 350
        x_gap = 260 if is_vert else 360
        strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㅈ 1획',
                        'clip_box': {'x': 40, 'y': y_top - 10, 'w': w_half, 'h': 70},
                        'd': f'M 50 {y_top + 30} L {w_half + 30} {y_top + 30}', 'width': 95, 'duration': 0.35})
        strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㅈ 2획',
                        'clip_box': {'x': 30, 'y': y_top + 20, 'w': w_half, 'h': y_bot - y_top},
                        'd': f'M {w_half // 2 + 30} {y_top + 30} C {w_half // 2 + 30} {y_top + 140} 120 {y_bot - 40} 50 {y_bot}', 'width': 95, 'duration': 0.5})
        strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㅈ 3획',
                        'clip_box': {'x': w_half // 2, 'y': y_top + 60, 'w': 100, 'h': y_bot - y_top - 40},
                        'd': f'M {w_half // 2 + 30} {y_top + 90} L {w_half + 30} {y_bot}', 'width': 95, 'duration': 0.45})
        strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㅈ 1획',
                        'clip_box': {'x': x_gap + 20, 'y': y_top - 10, 'w': w_half, 'h': 70},
                        'd': f'M {x_gap + 30} {y_top + 30} L {x_gap + w_half + 20} {y_top + 30}', 'width': 95, 'duration': 0.35})
        strokes.append({'order': ord_num + 4, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㅈ 2획',
                        'clip_box': {'x': x_gap + 10, 'y': y_top + 20, 'w': w_half, 'h': y_bot - y_top},
                        'd': f'M {x_gap + w_half // 2 + 20} {y_top + 30} C {x_gap + w_half // 2 + 20} {y_top + 140} {x_gap + 80} {y_bot - 40} {x_gap + 20} {y_bot}', 'width': 95, 'duration': 0.5})
        strokes.append({'order': ord_num + 5, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㅈ 3획',
                        'clip_box': {'x': x_gap + w_half // 2, 'y': y_top + 60, 'w': 110, 'h': y_bot - y_top - 40},
                        'd': f'M {x_gap + w_half // 2 + 20} {y_top + 90} L {x_gap + w_half + 30} {y_bot}', 'width': 95, 'duration': 0.45})

    # --- ㅊ ---
    elif cho == 'ㅊ':
        if archetype == 'H1' and jung in ('ㅜ', 'ㅠ'):
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 1획 (상단 꼭지)',
                            'clip_box': {'x': 400, 'y': 45, 'w': 120, 'h': 110}, 'd': 'M 459 45 L 459 135', 'width': 100, 'duration': 0.28})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 2획 (가로선)',
                            'clip_box': {'x': 90, 'y': 100, 'w': 740, 'h': 155}, 'd': 'M 105 168 L 810 168', 'width': 135, 'duration': 0.4})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 3획 (좌측 빗침)',
                            'clip_box': {'x': 60, 'y': 170, 'w': 430, 'h': 370}, 'd': 'M 459 200 C 420 300 280 440 95 530', 'width': 140, 'duration': 0.55})
            strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 4획 (우측 빗침)',
                            'clip_box': {'x': 430, 'y': 170, 'w': 430, 'h': 370}, 'd': 'M 459 200 C 500 300 640 440 820 530', 'width': 140, 'duration': 0.55})
        elif is_vert:
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 1획 (상단 꼭지)',
                            'clip_box': {'x': 270, 'y': 60, 'w': 90, 'h': 110}, 'd': 'M 312 65 L 312 150', 'width': 100, 'duration': 0.28})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 2획 (가로선)',
                            'clip_box': {'x': 70, 'y': 140, 'w': 530, 'h': 95}, 'd': 'M 90 185 L 575 185', 'width': 105, 'duration': 0.4})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 3획 (수직-곡선 빗침)',
                            'clip_box': {'x': 25, 'y': 180, 'w': 350, 'h': y_bot - 140},
                            'd': f'M 312 185 L 312 320 C 312 520 200 {y_bot - 60} 50 {y_bot}', 'width': 115, 'duration': 0.6})
            strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 4획 (우측 빗침)',
                            'clip_box': {'x': 280, 'y': 380, 'w': w_right - 260, 'h': y_bot - 340},
                            'd': f'M 312 430 L {w_right} {y_bot}', 'width': 115, 'duration': 0.55})
        else:
            y_b = 440 if archetype == 'H2' else 464
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 1획 (상단 꼭지)',
                            'clip_box': {'x': 420, 'y': 45, 'w': 80, 'h': 90}, 'd': 'M 459 45 L 459 125', 'width': 100, 'duration': 0.28})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 2획 (가로선)',
                            'clip_box': {'x': 130, 'y': 115, 'w': 660, 'h': 90}, 'd': 'M 140 160 L 780 160', 'width': 105, 'duration': 0.4})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 3획 (좌측 빗침)',
                            'clip_box': {'x': 70, 'y': 150, 'w': 410, 'h': y_b - 130},
                            'd': f'M 459 160 C 459 260 320 380 100 {y_b}', 'width': 110, 'duration': 0.55})
            strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 4획 (우측 빗침)',
                            'clip_box': {'x': 440, 'y': 180, 'w': 410, 'h': y_b - 160},
                            'd': f'M 460 250 C 500 300 650 390 815 {y_b}', 'width': 110, 'duration': 0.55})

    # --- ㅋ ---
    elif cho == 'ㅋ':
        if is_vert:
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅋ 1획 (상단 꺾음)',
                            'clip_box': {'x': 50, 'y': y_top - 10, 'w': 470, 'h': y_bot - y_top + 30},
                            'd': f'M 80 {y_top + 45} L 485 {y_top + 45} C 470 {y_top + 260} 360 {y_bot - 60} 55 {y_bot}', 'width': 105, 'duration': 0.65})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅋ 2획 (중간 가로)',
                            'clip_box': {'x': 60, 'y': y_top + 140, 'w': 380, 'h': 90},
                            'd': f'M 80 {y_top + 185} L 430 {y_top + 185}', 'width': 105, 'duration': 0.35})
        else:
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅋ 1획 (상단 꺾음)',
                            'clip_box': {'x': 120, 'y': y_top - 10, 'w': 670, 'h': y_bot - y_top + 30},
                            'd': f'M 130 {y_top + 45} L 725 {y_top + 45} C 725 {y_top + 200} 725 {y_bot - 40} 690 {y_bot}', 'width': 120, 'duration': 0.6})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅋ 2획 (중간 가로)',
                            'clip_box': {'x': 130, 'y': y_top + 120, 'w': 580, 'h': 90},
                            'd': f'M 140 {y_top + 165} L 700 {y_top + 165}', 'width': 105, 'duration': 0.35})

    # --- ㅌ ---
    elif cho == 'ㅌ':
        if archetype == 'H1' and jung in ('ㅜ', 'ㅠ'):
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 1획 (상단 가로)',
                            'clip_box': {'x': 140, 'y': 80, 'w': 660, 'h': 110}, 'd': 'M 150 130 L 780 130', 'width': 110, 'duration': 0.4})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 2획 (중간 가로)',
                            'clip_box': {'x': 140, 'y': 230, 'w': 660, 'h': 100}, 'd': 'M 150 280 L 780 280', 'width': 105, 'duration': 0.35})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 3획 (하단 ㄴ)',
                            'clip_box': {'x': 140, 'y': 120, 'w': 660, 'h': 350}, 'd': 'M 195 120 L 195 440 L 780 440', 'width': 115, 'duration': 0.55})
        else:
            w_b = w_right - 60
            y_mid = y_top + int((y_bot - y_top) * 0.45)
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 1획 (상단 가로)',
                            'clip_box': {'x': 70, 'y': y_top - 15, 'w': w_b + 50, 'h': 85},
                            'd': f'M 80 {y_top + 25} L {w_right} {y_top + 25}', 'width': 105, 'duration': 0.4})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 2획 (중간 가로)',
                            'clip_box': {'x': 70, 'y': y_mid - 40, 'w': w_b + 50, 'h': 80},
                            'd': f'M 120 {y_mid} L {w_right} {y_mid}', 'width': 100, 'duration': 0.35})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 3획 (하단 ㄴ)',
                            'clip_box': {'x': 70, 'y': y_mid + 20, 'w': w_b + 50, 'h': y_bot - y_mid + 20},
                            'd': f'M 130 {y_mid + 10} L 130 {y_bot} L {w_right} {y_bot}', 'width': 110, 'duration': 0.55})

    # --- ㅍ ---
    elif cho == 'ㅍ':
        if archetype == 'H1' and jung in ('ㅜ', 'ㅠ'):
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 1획 (상단 가로)',
                            'clip_box': {'x': 100, 'y': 80, 'w': 720, 'h': 110}, 'd': 'M 110 135 L 810 135', 'width': 110, 'duration': 0.4})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 2획 (좌측 세로)',
                            'clip_box': {'x': 250, 'y': 130, 'w': 140, 'h': 350}, 'd': 'M 310 130 L 310 440', 'width': 110, 'duration': 0.35})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 3획 (우측 세로)',
                            'clip_box': {'x': 530, 'y': 130, 'w': 140, 'h': 350}, 'd': 'M 590 130 L 590 440', 'width': 110, 'duration': 0.35})
            strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 4획 (하단 가로)',
                            'clip_box': {'x': 100, 'y': 380, 'w': 720, 'h': 100}, 'd': 'M 110 435 L 810 435', 'width': 110, 'duration': 0.4})
        else:
            w_b = w_right - 60
            x_l = 80 + int(w_b * 0.3)
            x_r = 80 + int(w_b * 0.7)
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 1획 (상단 가로)',
                            'clip_box': {'x': 70, 'y': y_top - 15, 'w': w_b + 50, 'h': 85},
                            'd': f'M 80 {y_top + 25} L {w_right} {y_top + 25}', 'width': 105, 'duration': 0.4})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 2획 (좌측 세로)',
                            'clip_box': {'x': x_l - 60, 'y': y_top + 20, 'w': 120, 'h': y_bot - y_top},
                            'd': f'M {x_l} {y_top + 25} L {x_l} {y_bot}', 'width': 100, 'duration': 0.4})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 3획 (우측 세로)',
                            'clip_box': {'x': x_r - 60, 'y': y_top + 20, 'w': 120, 'h': y_bot - y_top},
                            'd': f'M {x_r} {y_top + 25} L {x_r} {y_bot}', 'width': 100, 'duration': 0.4})
            strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 4획 (하단 가로)',
                            'clip_box': {'x': 70, 'y': y_bot - 45, 'w': w_b + 50, 'h': 85},
                            'd': f'M 80 {y_bot} L {w_right} {y_bot}', 'width': 105, 'duration': 0.4})

    # --- ㅎ ---
    elif cho == 'ㅎ':
        if archetype == 'V1':
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 1획 (상단 꼭지)',
                            'clip_box': {'x': 240, 'y': 45, 'w': 145, 'h': 140}, 'd': 'M 312 65 L 312 150', 'width': 120, 'duration': 0.28})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 2획 (가로선)',
                            'clip_box': {'x': 40, 'y': 130, 'w': 560, 'h': 160}, 'd': 'M 80 200 L 550 200', 'width': 125, 'duration': 0.45})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 3획 (원형 폐곡선)',
                            'clip_box': {'x': 40, 'y': 240, 'w': 540, 'h': 540}, 'd': 'M 312 285 A 165 230 0 1 0 312 745 A 165 230 0 1 0 312 285', 'width': 135, 'duration': 0.8})
        elif archetype == 'V2':
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 1획 (상단 꼭지)',
                            'clip_box': {'x': 270, 'y': 60, 'w': 80, 'h': 100}, 'd': 'M 312 65 L 312 140', 'width': 95, 'duration': 0.28})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 2획 (가로선)',
                            'clip_box': {'x': 60, 'y': 140, 'w': 510, 'h': 115}, 'd': 'M 70 185 L 560 185', 'width': 105, 'duration': 0.45})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 3획 (원형 폐곡선)',
                            'clip_box': {'x': 100, 'y': 250, 'w': 430, 'h': 340}, 'd': 'M 312 280 A 160 150 0 1 0 312 580 A 160 150 0 1 0 312 280', 'width': 115, 'duration': 0.75})
        else:
            y_c = 280 if archetype in ('H2', 'H1') and jung in ('ㅜ', 'ㅠ') else 320
            strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 1획 (상단 꼭지)',
                            'clip_box': {'x': 420, 'y': 50, 'w': 80, 'h': 90}, 'd': 'M 459 50 L 459 130', 'width': 95, 'duration': 0.28})
            strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 2획 (가로선)',
                            'clip_box': {'x': 120, 'y': 115, 'w': 680, 'h': 110}, 'd': 'M 130 160 L 790 160', 'width': 110, 'duration': 0.45})
            strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 3획 (원형 폐곡선)',
                            'clip_box': {'x': 250, 'y': 200, 'w': 420, 'h': 240}, 'd': f'M 460 {y_c - 100} A 140 100 0 1 0 460 {y_c + 100} A 140 100 0 1 0 460 {y_c - 100}', 'width': 105, 'duration': 0.75})

    return strokes


def get_jung_strokes(jung: str, archetype: str, start_order: int, cho: str = '', jong: str = '') -> List[Dict[str, Any]]:
    strokes = []
    ord_num = start_order
    is_vert = archetype in ('V1', 'V2')
    has_jong = archetype in ('V2', 'H2', 'C2')

    if is_vert:
        y_top = 45
        stem_x = 750 if archetype == 'V2' else 703
        y_bot = 725 if has_jong else 960
        b_w = 895

        if jung == 'ㅏ':
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 1획 (세로 기둥)',
                'clip_box': {'x': stem_x - 85, 'y': y_top, 'w': 170, 'h': y_bot - y_top + 15},
                'd': f'M {stem_x} {y_top} L {stem_x} {y_bot}', 'width': 110, 'duration': 0.65
            })
            b_y = 360 if has_jong else 454
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 2획 (우측 가로)',
                'clip_box': {'x': stem_x + 10, 'y': b_y - 55, 'w': b_w - stem_x + 30, 'h': 110},
                'd': f'M {stem_x} {b_y} L {b_w} {b_y}', 'width': 105, 'duration': 0.3
            })

        elif jung == 'ㅑ':
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅑ 1획 (세로 기둥)',
                'clip_box': {'x': stem_x - 60, 'y': y_top, 'w': 120, 'h': y_bot - y_top + 15},
                'd': f'M {stem_x} {y_top} L {stem_x} {y_bot}', 'width': 110, 'duration': 0.65
            })
            b1_y = 250 if has_jong else 350
            b2_y = 390 if has_jong else 560
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅑ 2획 (상단 가지)',
                'clip_box': {'x': stem_x + 25, 'y': b1_y - 35, 'w': b_w - stem_x + 20, 'h': 70},
                'd': f'M {stem_x} {b1_y} L {b_w} {b1_y}', 'width': 95, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅑ 3획 (하단 가지)',
                'clip_box': {'x': stem_x + 25, 'y': b2_y - 35, 'w': b_w - stem_x + 20, 'h': 70},
                'd': f'M {stem_x} {b2_y} L {b_w} {b2_y}', 'width': 95, 'duration': 0.3
            })

        elif jung == 'ㅓ':
            b_y = 360 if has_jong else 454
            x_c_start = 450
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 1획 (좌측 가로)',
                'clip_box': {'x': x_c_start, 'y': b_y - 50, 'w': stem_x - x_c_start + 30, 'h': 100},
                'd': f'M {x_c_start} {b_y} L {stem_x + 15} {b_y}', 'width': 105, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 2획 (세로 기둥)',
                'clip_box': {'x': stem_x - 60, 'y': y_top, 'w': 120, 'h': y_bot - y_top + 15},
                'd': f'M {stem_x} {y_top} L {stem_x} {y_bot}', 'width': 110, 'duration': 0.65
            })

        elif jung == 'ㅕ':
            b1_y = 230 if has_jong else 350
            b2_y = 390 if has_jong else 560
            x_c_start = 450
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 1획 (상단 가로)',
                'clip_box': {'x': x_c_start, 'y': b1_y - 40, 'w': stem_x - x_c_start + 30, 'h': 80},
                'd': f'M {x_c_start} {b1_y} L {stem_x + 15} {b1_y}', 'width': 95, 'duration': 0.32
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 2획 (하단 가로)',
                'clip_box': {'x': x_c_start, 'y': b2_y - 40, 'w': stem_x - x_c_start + 30, 'h': 80},
                'd': f'M {x_c_start} {b2_y} L {stem_x + 15} {b2_y}', 'width': 95, 'duration': 0.32
            })
            strokes.append({
                'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 3획 (세로 기둥)',
                'clip_box': {'x': stem_x - 60, 'y': y_top, 'w': 120, 'h': y_bot - y_top + 15},
                'd': f'M {stem_x} {y_top} L {stem_x} {y_bot}', 'width': 110, 'duration': 0.55
            })

        elif jung == 'ㅣ':
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅣ (세로 기둥)',
                'clip_box': {'x': stem_x - 65, 'y': y_top, 'w': 130, 'h': y_bot - y_top + 15},
                'd': f'M {stem_x} {y_top} L {stem_x} {y_bot}', 'width': 115, 'duration': 0.65
            })

        elif jung in ('ㅐ', 'ㅔ'):
            s1_x, s2_x = 585, 775
            b_y = 317 if has_jong else 454
            if jung == 'ㅐ':
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅐ 1획 (첫째 기둥)',
                    'clip_box': {'x': 520, 'y': y_top, 'w': 120, 'h': y_bot - y_top + 15},
                    'd': f'M {s1_x} {y_top} L {s1_x} {y_bot}', 'width': 105, 'duration': 0.55
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅐ 2획 (연결 가로)',
                    'clip_box': {'x': 565, 'y': b_y - 45, 'w': 190, 'h': 90},
                    'd': f'M {s1_x} {b_y} L {s2_x} {b_y}', 'width': 100, 'duration': 0.3
                })
                strokes.append({
                    'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅐ 3획 (둘째 기둥)',
                    'clip_box': {'x': 720, 'y': y_top, 'w': 120, 'h': y_bot - y_top + 15},
                    'd': f'M {s2_x} {y_top} L {s2_x} {y_bot}', 'width': 105, 'duration': 0.55
                })
            else:
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅔ 1획 (좌측 가로)',
                    'clip_box': {'x': 450, 'y': b_y - 45, 'w': 170, 'h': 90},
                    'd': f'M 460 {b_y} L {s1_x} {b_y}', 'width': 100, 'duration': 0.3
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅔ 2획 (첫째 기둥)',
                    'clip_box': {'x': 520, 'y': y_top, 'w': 120, 'h': y_bot - y_top + 15},
                    'd': f'M {s1_x} {y_top} L {s1_x} {y_bot}', 'width': 105, 'duration': 0.55
                })
                strokes.append({
                    'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅔ 3획 (둘째 기둥)',
                    'clip_box': {'x': 720, 'y': y_top, 'w': 120, 'h': y_bot - y_top + 15},
                    'd': f'M {s2_x} {y_top} L {s2_x} {y_bot}', 'width': 105, 'duration': 0.55
                })

    elif archetype in ('H1', 'H2'):
        if jung == 'ㅡ':
            bar_y = 792 if archetype == 'H1' else (465 if jong == 'ㄹ' else 550)
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅡ (긴 가로선)',
                'clip_box': {'x': 40, 'y': bar_y - 65, 'w': 840, 'h': 130},
                'd': f'M 40 {bar_y} L 880 {bar_y}', 'width': 115, 'duration': 0.5
            })

        elif jung == 'ㅗ':
            if archetype == 'H1':
                stub_x = 409 if cho == 'ㄱ' else 458
                stub_top = 430 if cho == 'ㄱ' else 540
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                    'clip_box': {'x': stub_x - 60, 'y': stub_top, 'w': 120, 'h': 775 - stub_top + 15},
                    'd': f'M {stub_x} {stub_top} L {stub_x} 775', 'width': 105, 'duration': 0.35
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가로선)',
                    'clip_box': {'x': 40, 'y': 740, 'w': 840, 'h': 110},
                    'd': 'M 40 796 L 880 796', 'width': 110, 'duration': 0.5
                })
            else: # H2 (곡, 꽃, 봄)
                stub_x = 476 if cho in ('ㄲ', 'ㅃ', 'ㅉ') else 427
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                    'clip_box': {'x': stub_x - 60, 'y': 280, 'w': 120, 'h': 215},
                    'd': f'M {stub_x} 280 L {stub_x} 495', 'width': 105, 'duration': 0.3
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가로선)',
                    'clip_box': {'x': 40, 'y': 430, 'w': 835, 'h': 135},
                    'd': 'M 40 495 L 875 495', 'width': 115, 'duration': 0.5
                })

        elif jung == 'ㅛ':
            bar_y = 796 if archetype == 'H1' else 472
            p_top = 420 if archetype == 'H1' else 280
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅛ 1획 (좌세로점)',
                'clip_box': {'x': 300, 'y': p_top, 'w': 100, 'h': bar_y - p_top + 10},
                'd': f'M 345 {p_top} L 345 {bar_y}', 'width': 90, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅛ 2획 (우세로점)',
                'clip_box': {'x': 520, 'y': p_top, 'w': 100, 'h': bar_y - p_top + 10},
                'd': f'M 565 {p_top} L 565 {bar_y}', 'width': 90, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅛ 3획 (가로선)',
                'clip_box': {'x': 40, 'y': bar_y - 50, 'w': 840, 'h': 110},
                'd': f'M 40 {bar_y} L 880 {bar_y}', 'width': 110, 'duration': 0.5
            })

        elif jung == 'ㅜ':
            if archetype == 'H1':
                bar_y = 535 if cho == 'ㄱ' else (635 if cho == 'ㅊ' else 610)
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가로선)',
                    'clip_box': {'x': 40, 'y': bar_y - 65, 'w': 840, 'h': 130},
                    'd': f'M 40 {bar_y} L 880 {bar_y}', 'width': 115, 'duration': 0.5
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                    'clip_box': {'x': 400, 'y': bar_y - 10, 'w': 120, 'h': 970 - bar_y + 10},
                    'd': f'M 459 {bar_y - 10} L 459 958', 'width': 115, 'duration': 0.35
                })
            else: # H2 (문, 눈, 물, 불)
                bar_y = 442 if jong == 'ㄹ' else 520
                p_y2 = 632 if jong == 'ㄹ' else 720
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가로선)',
                    'clip_box': {'x': 40, 'y': bar_y - 55, 'w': 840, 'h': 115},
                    'd': f'M 46 {bar_y} L 875 {bar_y}', 'width': 110, 'duration': 0.5
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                    'clip_box': {'x': 410, 'y': bar_y - 10, 'w': 100, 'h': p_y2 - bar_y + 20},
                    'd': f'M 457 {bar_y} L 457 {p_y2}', 'width': 105, 'duration': 0.3
                })

        elif jung == 'ㅠ':
            if archetype == 'H1':
                bar_y = 610
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅠ 1획 (가로선)',
                    'clip_box': {'x': 40, 'y': bar_y - 65, 'w': 840, 'h': 130},
                    'd': f'M 40 {bar_y} L 880 {bar_y}', 'width': 115, 'duration': 0.5
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅠ 2획 (좌세로점)',
                    'clip_box': {'x': 320, 'y': bar_y - 10, 'w': 90, 'h': 970 - bar_y + 10},
                    'd': f'M 365 {bar_y} L 365 958', 'width': 105, 'duration': 0.35
                })
                strokes.append({
                    'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅠ 3획 (우세로점)',
                    'clip_box': {'x': 540, 'y': bar_y - 10, 'w': 90, 'h': 970 - bar_y + 10},
                    'd': f'M 585 {bar_y} L 585 958', 'width': 105, 'duration': 0.35
                })

    else: # Compound vowels (C1, C2)
        is_c1 = (archetype == 'C1')
        h_part = 'ㅗ' if jung in ('ㅘ', 'ㅙ', 'ㅚ') else ('ㅜ' if jung in ('ㅝ', 'ㅞ', 'ㅟ') else 'ㅡ')
        v_part = 'ㅏ' if jung in ('ㅘ', 'ㅙ') else ('ㅓ' if jung in ('ㅝ', 'ㅞ') else 'ㅣ')

        if h_part == 'ㅗ':
            if cho == 'ㄱ':
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                    'clip_box': {'x': 270, 'y': 250, 'w': 100, 'h': 240},
                    'd': 'M 319 250 L 319 490', 'width': 95, 'duration': 0.35
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가로선)',
                    'clip_box': {'x': 40, 'y': 440, 'w': 570, 'h': 120},
                    'd': 'M 40 495 L 610 495', 'width': 105, 'duration': 0.5
                })
            else:
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                    'clip_box': {'x': 225, 'y': 335, 'w': 115, 'h': 235},
                    'd': 'M 283 335 L 283 570', 'width': 100, 'duration': 0.35
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가로선)',
                    'clip_box': {'x': 35, 'y': 525, 'w': 585, 'h': 115},
                    'd': 'M 35 582 L 615 582', 'width': 100, 'duration': 0.5
                })
            ord_num += 2

        elif h_part == 'ㅜ':
            y_b = 600 if is_c1 else 480
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가로선)',
                'clip_box': {'x': 40, 'y': y_b - 50, 'w': 580, 'h': 100},
                'd': f'M 40 {y_b} L 600 {y_b}', 'width': 100, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                'clip_box': {'x': 280, 'y': y_b, 'w': 100, 'h': 180},
                'd': f'M 330 {y_b} L 330 {y_b + 170}', 'width': 95, 'duration': 0.3
            })
            ord_num += 2

        else: # 'ㅡ' (ㅢ)
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅡ (긴 가로선)',
                'clip_box': {'x': 40, 'y': 650, 'w': 620, 'h': 120},
                'd': 'M 40 710 L 650 710', 'width': 105, 'duration': 0.5
            })
            ord_num += 1

        v_stem_x = 710
        y_v_bot = 960 if is_c1 else 660

        if v_part == 'ㅏ':
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 1획 (세로 기둥)',
                'clip_box': {'x': v_stem_x - 50, 'y': 45, 'w': 100, 'h': y_v_bot - 30},
                'd': f'M {v_stem_x} 45 L {v_stem_x} {y_v_bot}', 'width': 105, 'duration': 0.6
            })
            b_y = 454 if is_c1 else 317
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 2획 (우측 가로)',
                'clip_box': {'x': v_stem_x + 30, 'y': b_y - 45, 'w': 180, 'h': 95},
                'd': f'M {v_stem_x} {b_y} L 890 {b_y}', 'width': 105, 'duration': 0.3
            })
        elif v_part == 'ㅓ':
            b_y = 454 if is_c1 else 317
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 1획 (좌측 가로)',
                'clip_box': {'x': v_stem_x - 180, 'y': b_y - 40, 'w': 190, 'h': 80},
                'd': f'M {v_stem_x - 170} {b_y} L {v_stem_x + 15} {b_y}', 'width': 95, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 2획 (세로 기둥)',
                'clip_box': {'x': v_stem_x - 50, 'y': 45, 'w': 100, 'h': y_v_bot - 30},
                'd': f'M {v_stem_x} 45 L {v_stem_x} {y_v_bot}', 'width': 105, 'duration': 0.6
            })
        else: # 'ㅣ'
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅣ (세로 기둥)',
                'clip_box': {'x': v_stem_x - 50, 'y': 45, 'w': 110, 'h': y_v_bot - 30},
                'd': f'M {v_stem_x} 45 L {v_stem_x} {y_v_bot}', 'width': 110, 'duration': 0.6
            })

    return strokes


def get_jong_strokes(jong: str, start_order: int, archetype: str = 'H2') -> List[Dict[str, Any]]:
    strokes = []
    ord_num = start_order
    is_v2 = (archetype == 'V2')

    # --- ㄱ ---
    if jong == 'ㄱ':
        y_t = 580 if is_v2 else 615
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㄱ 받침 (직각 꺾음)',
            'clip_box': {'x': 130, 'y': y_t, 'w': 645, 'h': 970 - y_t},
            'd': f'M 130 {y_t + 55} L 725 {y_t + 55} L 725 965', 'width': 125, 'duration': 0.65
        })

    # --- ㄴ ---
    elif jong == 'ㄴ':
        if is_v2:
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㄴ 받침 (세로-가로 꺾음)',
                'clip_box': {'x': 170, 'y': 600, 'w': 660, 'h': 350},
                'd': 'M 240 640 L 240 895 L 815 895', 'width': 120, 'duration': 0.65
            })
        else:
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㄴ 받침 (세로-가로 꺾음)',
                'clip_box': {'x': 130, 'y': 650, 'w': 670, 'h': 300},
                'd': 'M 195 660 L 195 900 L 790 900', 'width': 120, 'duration': 0.65
            })

    # --- ㄹ ---
    elif jong == 'ㄹ':
        y_base = 580 if is_v2 else 587
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㄹ 받침 1획 (상단 ㄱ)',
            'clip_box': {'x': 130, 'y': y_base - 25, 'w': 720, 'h': 190},
            'd': f'M 140 {y_base + 23} L 755 {y_base + 23} L 752 {y_base + 153}', 'width': 115, 'duration': 0.5
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㄹ 받침 2획 (중간 가로)',
            'clip_box': {'x': 130, 'y': y_base + 120, 'w': 720, 'h': 85},
            'd': f'M 140 {y_base + 168} L 805 {y_base + 168}', 'width': 110, 'duration': 0.4
        })
        strokes.append({
            'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㄹ 받침 3획 (하단 ㄴ)',
            'clip_box': {'x': 130, 'y': y_base + 175, 'w': 720, 'h': 210},
            'd': f'M 190 {y_base + 175} L 190 920 L 835 920', 'width': 115, 'duration': 0.55
        })

    # --- ㅁ ---
    elif jong == 'ㅁ':
        y_m = 580 if is_v2 else 610
        strokes.append({'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅁ 받침 1획 (좌측 세로)',
                        'clip_box': {'x': 160, 'y': y_m, 'w': 140, 'h': 950 - y_m}, 'd': f'M 200 {y_m} L 200 910', 'width': 110, 'duration': 0.4})
        strokes.append({'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅁ 받침 2획 (상단-우측 꺾음)',
                        'clip_box': {'x': 200, 'y': y_m, 'w': 620, 'h': 950 - y_m}, 'd': f'M 200 {y_m + 50} L 760 {y_m + 50} L 760 910', 'width': 110, 'duration': 0.55})
        strokes.append({'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㅁ 받침 3획 (하단 가로)',
                        'clip_box': {'x': 200, 'y': 860, 'w': 620, 'h': 90}, 'd': 'M 200 910 L 760 910', 'width': 110, 'duration': 0.35})

    # --- ㅂ ---
    elif jong == 'ㅂ':
        y_b = 580 if is_v2 else 600
        strokes.append({'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅂ 받침 1획 (좌측 기둥)',
                        'clip_box': {'x': 160, 'y': y_b, 'w': 140, 'h': 950 - y_b}, 'd': f'M 200 {y_b} L 200 915', 'width': 110, 'duration': 0.45})
        strokes.append({'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅂ 받침 2획 (우측 기둥)',
                        'clip_box': {'x': 700, 'y': y_b, 'w': 140, 'h': 950 - y_b}, 'd': f'M 740 {y_b} L 740 915', 'width': 110, 'duration': 0.45})
        strokes.append({'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㅂ 받침 3획 (중간 가로)',
                        'clip_box': {'x': 200, 'y': 710, 'w': 540, 'h': 90}, 'd': 'M 200 755 L 740 755', 'width': 105, 'duration': 0.35})
        strokes.append({'order': ord_num + 3, 'part': '종성', 'color': '#a855f7', 'name': 'ㅂ 받침 4획 (하단 가로)',
                        'clip_box': {'x': 200, 'y': 870, 'w': 540, 'h': 80}, 'd': 'M 200 915 L 740 915', 'width': 110, 'duration': 0.35})

    # --- ㅅ ---
    elif jong == 'ㅅ':
        strokes.append({'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅅ 받침 1획 (좌측 빗침)',
                        'clip_box': {'x': 90, 'y': 580, 'w': 400, 'h': 380}, 'd': 'M 459 620 C 459 750 320 890 100 930', 'width': 115, 'duration': 0.55})
        strokes.append({'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅅ 받침 2획 (우측 빗침)',
                        'clip_box': {'x': 440, 'y': 690, 'w': 420, 'h': 270}, 'd': 'M 460 720 C 500 780 650 890 825 930', 'width': 115, 'duration': 0.5})

    # --- ㅆ ---
    elif jong == 'ㅆ':
        for offset, prefix in [(0, '첫째 ㅅ 받침'), (360, '둘째 ㅅ 받침')]:
            strokes.append({'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{prefix} 1획',
                            'clip_box': {'x': 60 + offset, 'y': 600, 'w': 280, 'h': 360},
                            'd': f'M {260 + offset} 630 C {260 + offset} 750 {150 + offset} 880 {80 + offset} 930', 'width': 100, 'duration': 0.45})
            strokes.append({'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': f'{prefix} 2획',
                            'clip_box': {'x': 240 + offset, 'y': 700, 'w': 140, 'h': 260},
                            'd': f'M {260 + offset} 730 L {350 + offset} 930', 'width': 100, 'duration': 0.4})
            ord_num += 2
        return strokes

    # --- ㅇ ---
    elif jong == 'ㅇ':
        y_o = 600 if is_v2 else 610
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅇ 받침 (원형 폐곡선)',
            'clip_box': {'x': 140, 'y': y_o - 20, 'w': 680, 'h': 970 - y_o},
            'd': f'M 459 {y_o + 20} A 240 160 0 1 0 459 950 A 240 160 0 1 0 459 {y_o + 20}', 'width': 120, 'duration': 0.8
        })

    # --- ㅊ ---
    elif jong == 'ㅊ':
        strokes.append({'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅊ 받침 1획 (상단 꼭지)',
                        'clip_box': {'x': 420, 'y': 540, 'w': 80, 'h': 85}, 'd': 'M 459 540 L 459 615', 'width': 95, 'duration': 0.28})
        strokes.append({'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅊ 받침 2획 (가로선)',
                        'clip_box': {'x': 110, 'y': 600, 'w': 700, 'h': 90}, 'd': 'M 120 645 L 800 645', 'width': 105, 'duration': 0.4})
        strokes.append({'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㅊ 받침 3획 (좌측 빗침)',
                        'clip_box': {'x': 90, 'y': 630, 'w': 400, 'h': 330}, 'd': 'M 459 645 C 459 760 320 890 100 930', 'width': 115, 'duration': 0.55})
        strokes.append({'order': ord_num + 3, 'part': '종성', 'color': '#a855f7', 'name': 'ㅊ 받침 4획 (우측 빗침)',
                        'clip_box': {'x': 440, 'y': 690, 'w': 420, 'h': 270}, 'd': 'M 460 720 C 500 780 650 890 825 930', 'width': 115, 'duration': 0.5})

    return strokes
