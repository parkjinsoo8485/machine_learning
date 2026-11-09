"""
Jamo Rules Library for Noto Sans CJK KR
=======================================
Defines canonical stroke orders, overshoot trajectories, and bounding box offsets
for all 19 Initial Consonants (Cho), 21 Vowels (Jung), and 27 Final Consonants (Jong)
across all structural layout archetypes (V1, V2, H1, H2, C1, C2).
"""

from typing import Dict, List, Any

CHO_LIST = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
JUNG_LIST = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
JONG_LIST = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

def get_cho_strokes(cho: str, archetype: str, start_order: int) -> List[Dict[str, Any]]:
    """Generates standard stroke order trajectories for Cho based on archetype."""
    strokes = []
    ord_num = start_order

    # Setup archetype bounding geometry
    if archetype == 'V1':
        y_top, y_bot, w_right = 120, 720, 570
        is_vert, has_jong = True, False
    elif archetype == 'V2':
        y_top, y_bot, w_right = 100, 525, 570
        is_vert, has_jong = True, True
    elif archetype == 'H1':
        y_top, y_bot, w_right = 120, 390, 770
        is_vert, has_jong = False, False
    elif archetype == 'H2':
        y_top, y_bot, w_right = 90, 360, 770
        is_vert, has_jong = False, True
    elif archetype == 'C1':
        y_top, y_bot, w_right = 110, 550, 540
        is_vert, has_jong = True, False
    else: # C2
        y_top, y_bot, w_right = 90, 400, 540
        is_vert, has_jong = True, True

    # --- ㄱ ---
    if cho == 'ㄱ':
        if archetype == 'V1':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (곡선 꺾음)',
                'clip_box': {'x': 50, 'y': 140, 'w': 470, 'h': 650},
                'd': 'M 90 185 L 485 185 C 470 400 360 620 55 755', 'width': 105, 'duration': 0.65
            })
        elif archetype == 'V2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (곡선 꺾음)',
                'clip_box': {'x': 40, 'y': 100, 'w': 480, 'h': 490},
                'd': 'M 80 145 L 475 145 C 475 320 340 490 55 560', 'width': 115, 'duration': 0.6
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
                'clip_box': {'x': 80, 'y': 100, 'w': 480, 'h': 320},
                'd': 'M 99 144 L 506 144 L 482 405', 'width': 105, 'duration': 0.55
            })
        elif archetype == 'H1':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (직각 꺾음)',
                'clip_box': {'x': 125, 'y': 130, 'w': 655, 'h': 535},
                'd': 'M 130 178 L 740 178 C 740 340, 740 460, 695 655', 'width': 115, 'duration': 0.6
            })
        else: # H2
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄱ (직각 꺾음)',
                'clip_box': {'x': 135, 'y': 90, 'w': 635, 'h': 340},
                'd': 'M 140 135 L 735 135 C 735 240, 735 320, 695 425', 'width': 115, 'duration': 0.6
            })

    # --- ㄲ ---
    elif cho == 'ㄲ':
        if not is_vert: # H1, H2
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': '첫째 ㄱ',
                'clip_box': {'x': 110, 'y': 80, 'w': 295, 'h': 315},
                'd': 'M 115 122 L 365 122 C 375 220, 360 320, 310 395', 'width': 125, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': '둘째 ㄱ',
                'clip_box': {'x': 460, 'y': 80, 'w': 325, 'h': 315},
                'd': 'M 460 122 L 745 122 C 755 220, 740 320, 690 395', 'width': 125, 'duration': 0.45
            })
        else: # V1, V2, C1, C2
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
        strokes.append({
            'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄴ (세로-가로 꺾음)',
            'clip_box': {'x': 80 if is_vert else 150, 'y': y_top - 10, 'w': w_right - (50 if is_vert else 100), 'h': y_bot - y_top + 40},
            'd': f'M 140 {y_top} L 140 {y_bot} L {w_right} {y_bot}' if is_vert else f'M 180 {y_top} L 180 {y_bot} L {w_right} {y_bot}',
            'width': 105, 'duration': 0.65
        })

    # --- ㄷ ---
    elif cho == 'ㄷ':
        if archetype == 'V2':
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                'clip_box': {'x': 80, 'y': 90, 'w': 510, 'h': 95},
                'd': 'M 90 140 L 575 140', 'width': 120, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                'clip_box': {'x': 80, 'y': 135, 'w': 510, 'h': 350},
                'd': 'M 145 135 L 145 440 L 575 440', 'width': 120, 'duration': 0.6
            })
        else:
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 1획 (상단 가로)',
                'clip_box': {'x': 80 if is_vert else 150, 'y': y_top - 20, 'w': w_right + 10, 'h': 90},
                'd': f'M 90 {y_top} L {w_right} {y_top}' if is_vert else f'M 150 {y_top} L {w_right} {y_top}',
                'width': 95, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
                'clip_box': {'x': 80 if is_vert else 150, 'y': y_top + 30, 'w': w_right + 10, 'h': y_bot - y_top + 30},
                'd': f'M 140 {y_top + 20} L 140 {y_bot} L {w_right} {y_bot}' if is_vert else f'M 180 {y_top + 20} L 180 {y_bot} L {w_right} {y_bot}',
                'width': 105, 'duration': 0.6
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
        y1 = y_top
        y2 = (y_top * 2 + y_bot) // 3
        y3 = y_bot
        strokes.append({
            'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 1획 (상단 ㄱ)',
            'clip_box': {'x': 80 if is_vert else 140, 'y': y1 - 20, 'w': w_right + 10, 'h': (y2 - y1) + 20},
            'd': f'M 90 {y1} L {w_right} {y1} L {w_right - 40} {y2}', 'width': 105, 'duration': 0.55
        })
        strokes.append({
            'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 2획 (중간 가로)',
            'clip_box': {'x': 80 if is_vert else 140, 'y': y2 - 20, 'w': w_right + 10, 'h': 80},
            'd': f'M 90 {y2} L {w_right} {y2}', 'width': 95, 'duration': 0.45
        })
        strokes.append({
            'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㄹ 3획 (하단 ㄴ)',
            'clip_box': {'x': 80 if is_vert else 140, 'y': y2 + 30, 'w': w_right + 10, 'h': (y3 - y2) + 30},
            'd': f'M 140 {y2 + 20} L 140 {y3} L {w_right} {y3}', 'width': 110, 'duration': 0.65
        })

    # --- ㅁ ---
    elif cho == 'ㅁ':
        strokes.append({
            'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 1획 (좌측 세로)',
            'clip_box': {'x': 80 if is_vert else 150, 'y': y_top - 20, 'w': 100, 'h': y_bot - y_top + 40},
            'd': f'M 140 {y_top} L 140 {y_bot}' if is_vert else f'M 190 {y_top} L 190 {y_bot}', 'width': 100, 'duration': 0.45
        })
        strokes.append({
            'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 2획 (상우 꺾음)',
            'clip_box': {'x': 180 if is_vert else 240, 'y': y_top - 20, 'w': w_right - 80, 'h': y_bot - y_top + 40},
            'd': f'M 140 {y_top} L {w_right} {y_top} L {w_right} {y_bot}' if is_vert else f'M 190 {y_top} L {w_right} {y_top} L {w_right} {y_bot}', 'width': 100, 'duration': 0.6
        })
        strokes.append({
            'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅁ 3획 (하단 가로)',
            'clip_box': {'x': 180 if is_vert else 240, 'y': y_bot - 40, 'w': w_right - 140, 'h': 80},
            'd': f'M 140 {y_bot} L {w_right} {y_bot}' if is_vert else f'M 190 {y_bot} L {w_right} {y_bot}', 'width': 95, 'duration': 0.4
        })

    # --- ㅂ ---
    elif cho == 'ㅂ':
        if archetype == 'V2':
            # Exact calibrated coordinates for V2 (별, 밥, etc.)
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 1획 (좌측 세로)',
                'clip_box': {'x': 90, 'y': 80, 'w': 95, 'h': 420},
                'd': 'M 135.5 80 L 135.5 500', 'width': 95, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 2획 (우측 세로)',
                'clip_box': {'x': 415, 'y': 80, 'w': 95, 'h': 420},
                'd': 'M 462 80 L 462 500', 'width': 95, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 3획 (중간 가로)',
                'clip_box': {'x': 170, 'y': 220, 'w': 260, 'h': 75},
                'd': 'M 170 256.5 L 430 256.5', 'width': 85, 'duration': 0.35
            })
            strokes.append({
                'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 4획 (하단 가로)',
                'clip_box': {'x': 170, 'y': 415, 'w': 260, 'h': 80},
                'd': 'M 170 455.5 L 430 455.5', 'width': 85, 'duration': 0.35
            })
        else:
            xl = 172 if is_vert else 240
            xr = 425 if is_vert else 700
            ym = (y_top + y_bot) // 2
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 1획 (좌측 세로)',
                'clip_box': {'x': xl - 45, 'y': y_top - 20, 'w': 90, 'h': y_bot - y_top + 40},
                'd': f'M {xl} {y_top} L {xl} {y_bot}', 'width': 100, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 2획 (우측 세로)',
                'clip_box': {'x': xr - 45, 'y': y_top - 20, 'w': 90, 'h': y_bot - y_top + 40},
                'd': f'M {xr} {y_top} L {xr} {y_bot}', 'width': 100, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 3획 (중간 가로)',
                'clip_box': {'x': xl + 20, 'y': ym - 36, 'w': xr - xl - 20, 'h': 72},
                'd': f'M {xl} {ym} L {xr} {ym}', 'width': 85, 'duration': 0.35
            })
            strokes.append({
                'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅂ 4획 (하단 가로)',
                'clip_box': {'x': xl + 20, 'y': y_bot - 45, 'w': xr - xl - 20, 'h': 72},
                'd': f'M {xl} {y_bot - 20} L {xr} {y_bot - 20}', 'width': 85, 'duration': 0.35
            })

    # --- ㅃ ---
    elif cho == 'ㅃ':
        w_half = 220 if is_vert else 300
        x_gap = 240 if is_vert else 340
        for idx, ox in enumerate([0, x_gap]):
            xl, xr = 90 + ox, 210 + ox
            ym = (y_top + y_bot) // 2
            pfx = '첫째 ' if idx == 0 else '둘째 '
            o = ord_num + idx * 4
            strokes.append({'order': o, 'part': '초성', 'color': '#3b82f6', 'name': pfx + 'ㅂ 1획',
                            'clip_box': {'x': xl - 30, 'y': y_top - 15, 'w': 65, 'h': y_bot - y_top + 30},
                            'd': f'M {xl} {y_top} L {xl} {y_bot}', 'width': 85, 'duration': 0.4})
            strokes.append({'order': o + 1, 'part': '초성', 'color': '#3b82f6', 'name': pfx + 'ㅂ 2획',
                            'clip_box': {'x': xr - 30, 'y': y_top - 15, 'w': 65, 'h': y_bot - y_top + 30},
                            'd': f'M {xr} {y_top} L {xr} {y_bot}', 'width': 85, 'duration': 0.4})
            strokes.append({'order': o + 2, 'part': '초성', 'color': '#3b82f6', 'name': pfx + 'ㅂ 3획',
                            'clip_box': {'x': xl + 15, 'y': ym - 25, 'w': xr - xl - 15, 'h': 55},
                            'd': f'M {xl} {ym} L {xr} {ym}', 'width': 75, 'duration': 0.3})
            strokes.append({'order': o + 3, 'part': '초성', 'color': '#3b82f6', 'name': pfx + 'ㅂ 4획',
                            'clip_box': {'x': xl + 15, 'y': y_bot - 40, 'w': xr - xl - 15, 'h': 60},
                            'd': f'M {xl} {y_bot - 20} L {xr} {y_bot - 20}', 'width': 75, 'duration': 0.3})

    # --- ㅅ ---
    elif cho == 'ㅅ':
        cx = 320 if is_vert else 460
        strokes.append({
            'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 1획 (좌측 빗침)',
            'clip_box': {'x': 80 if is_vert else 130, 'y': y_top - 15, 'w': cx - (50 if is_vert else 100), 'h': y_bot - y_top + 35},
            'd': f'M {cx} {y_top} L {80 if is_vert else 140} {y_bot}', 'width': 105, 'duration': 0.55
        })
        strokes.append({
            'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅅ 2획 (우측 빗침)',
            'clip_box': {'x': cx - 20, 'y': y_top + 20, 'w': w_right - cx + 40, 'h': y_bot - y_top},
            'd': f'M {cx - 15} {y_top + 80} L {w_right} {y_bot}', 'width': 105, 'duration': 0.55
        })

    # --- ㅆ ---
    elif cho == 'ㅆ':
        for idx, ox in enumerate([0, 230 if is_vert else 310]):
            cx = (210 if is_vert else 280) + ox
            pfx = '첫째 ' if idx == 0 else '둘째 '
            o = ord_num + idx * 2
            strokes.append({'order': o, 'part': '초성', 'color': '#3b82f6', 'name': pfx + 'ㅅ 1획',
                            'clip_box': {'x': cx - 120, 'y': y_top - 15, 'w': 130, 'h': y_bot - y_top + 35},
                            'd': f'M {cx} {y_top} L {cx - 110} {y_bot}', 'width': 95, 'duration': 0.5})
            strokes.append({'order': o + 1, 'part': '초성', 'color': '#3b82f6', 'name': pfx + 'ㅅ 2획',
                            'clip_box': {'x': cx - 15, 'y': y_top + 20, 'w': 130, 'h': y_bot - y_top},
                            'd': f'M {cx - 15} {y_top + 60} L {cx + 105} {y_bot}', 'width': 95, 'duration': 0.5})

    # --- ㅇ ---
    elif cho == 'ㅇ':
        cx = 320 if is_vert else 460
        cy = (y_top + y_bot) // 2
        rx = 180 if is_vert else 240
        ry = (y_bot - y_top) // 2
        strokes.append({
            'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅇ (원형 폐곡선)',
            'clip_box': {'x': cx - rx - 25, 'y': cy - ry - 25, 'w': rx * 2 + 50, 'h': ry * 2 + 50},
            'd': f'M {cx} {cy - ry} A {rx} {ry} 0 1 0 {cx} {cy + ry} A {rx} {ry} 0 1 0 {cx} {cy - ry}',
            'width': 115, 'duration': 0.75
        })

    # --- ㅈ ---
    elif cho == 'ㅈ':
        cx = 320 if is_vert else 460
        strokes.append({
            'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 1획 (가로선)',
            'clip_box': {'x': 80 if is_vert else 140, 'y': y_top - 20, 'w': w_right + 10, 'h': 75},
            'd': f'M 90 {y_top} L {w_right} {y_top}', 'width': 95, 'duration': 0.4
        })
        strokes.append({
            'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 2획 (좌측 빗침)',
            'clip_box': {'x': 80 if is_vert else 130, 'y': y_top + 10, 'w': cx - (50 if is_vert else 100), 'h': y_bot - y_top + 10},
            'd': f'M {cx} {y_top} L {80 if is_vert else 140} {y_bot}', 'width': 105, 'duration': 0.55
        })
        strokes.append({
            'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅈ 3획 (우측 빗침)',
            'clip_box': {'x': cx - 20, 'y': y_top + 20, 'w': w_right - cx + 40, 'h': y_bot - y_top},
            'd': f'M {cx - 15} {y_top + 80} L {w_right} {y_bot}', 'width': 105, 'duration': 0.55
        })

    # --- ㅉ ---
    elif cho == 'ㅉ':
        for idx, ox in enumerate([0, 230 if is_vert else 310]):
            cx = (210 if is_vert else 280) + ox
            pfx = '첫째 ' if idx == 0 else '둘째 '
            o = ord_num + idx * 3
            strokes.append({'order': o, 'part': '초성', 'color': '#3b82f6', 'name': pfx + 'ㅈ 1획',
                            'clip_box': {'x': cx - 120, 'y': y_top - 15, 'w': 240, 'h': 65},
                            'd': f'M {cx - 110} {y_top} L {cx + 110} {y_top}', 'width': 85, 'duration': 0.35})
            strokes.append({'order': o + 1, 'part': '초성', 'color': '#3b82f6', 'name': pfx + 'ㅈ 2획',
                            'clip_box': {'x': cx - 120, 'y': y_top + 10, 'w': 130, 'h': y_bot - y_top + 10},
                            'd': f'M {cx} {y_top} L {cx - 110} {y_bot}', 'width': 90, 'duration': 0.45})
            strokes.append({'order': o + 2, 'part': '초성', 'color': '#3b82f6', 'name': pfx + 'ㅈ 3획',
                            'clip_box': {'x': cx - 15, 'y': y_top + 20, 'w': 130, 'h': y_bot - y_top},
                            'd': f'M {cx - 15} {y_top + 60} L {cx + 105} {y_bot}', 'width': 90, 'duration': 0.45})

    # --- ㅊ ---
    elif cho == 'ㅊ':
        cx = 320 if is_vert else 460
        strokes.append({
            'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 1획 (상단 꼭지)',
            'clip_box': {'x': cx - 50, 'y': y_top - 35, 'w': 100, 'h': 65},
            'd': f'M {cx} {y_top - 35} L {cx} {y_top + 15}', 'width': 95, 'duration': 0.28
        })
        strokes.append({
            'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 2획 (가로선)',
            'clip_box': {'x': 80 if is_vert else 140, 'y': y_top + 10, 'w': w_right + 10, 'h': 75},
            'd': f'M 90 {y_top + 30} L {w_right} {y_top + 30}', 'width': 95, 'duration': 0.4
        })
        strokes.append({
            'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 3획 (좌측 빗침)',
            'clip_box': {'x': 80 if is_vert else 130, 'y': y_top + 35, 'w': cx - (50 if is_vert else 100), 'h': y_bot - y_top + 10},
            'd': f'M {cx} {y_top + 30} L {80 if is_vert else 140} {y_bot}', 'width': 105, 'duration': 0.55
        })
        strokes.append({
            'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅊ 4획 (우측 빗침)',
            'clip_box': {'x': cx - 20, 'y': y_top + 45, 'w': w_right - cx + 40, 'h': y_bot - y_top},
            'd': f'M {cx - 15} {y_top + 100} L {w_right} {y_bot}', 'width': 105, 'duration': 0.55
        })

    # --- ㅋ ---
    elif cho == 'ㅋ':
        y_mid = (y_top + y_bot) // 2
        strokes.append({
            'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅋ 1획 (ㄱ 꺾음)',
            'clip_box': {'x': 80 if is_vert else 135, 'y': y_top - 20, 'w': w_right + 10, 'h': y_bot - y_top + 30},
            'd': f'M 90 {y_top} L {w_right} {y_top} L {w_right - 40} {y_bot}', 'width': 105, 'duration': 0.6
        })
        strokes.append({
            'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅋ 2획 (중간 가로)',
            'clip_box': {'x': 80 if is_vert else 135, 'y': y_mid - 35, 'w': w_right - 40, 'h': 75},
            'd': f'M 90 {y_mid} L {w_right - 50} {y_mid}', 'width': 95, 'duration': 0.4
        })

    # --- ㅌ ---
    elif cho == 'ㅌ':
        y_mid = (y_top + y_bot) // 2
        strokes.append({
            'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 1획 (상단 가로)',
            'clip_box': {'x': 80 if is_vert else 150, 'y': y_top - 20, 'w': w_right + 10, 'h': 75},
            'd': f'M 90 {y_top} L {w_right} {y_top}' if is_vert else f'M 150 {y_top} L {w_right} {y_top}',
            'width': 95, 'duration': 0.4
        })
        strokes.append({
            'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 2획 (중간 가로)',
            'clip_box': {'x': 80 if is_vert else 150, 'y': y_mid - 35, 'w': w_right + 10, 'h': 75},
            'd': f'M 90 {y_mid} L {w_right} {y_mid}' if is_vert else f'M 150 {y_mid} L {w_right} {y_mid}',
            'width': 90, 'duration': 0.4
        })
        strokes.append({
            'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅌ 3획 (하단 ㄴ 꺾음)',
            'clip_box': {'x': 80 if is_vert else 150, 'y': y_mid + 30, 'w': w_right + 10, 'h': y_bot - y_mid + 30},
            'd': f'M 140 {y_mid + 20} L 140 {y_bot} L {w_right} {y_bot}' if is_vert else f'M 180 {y_mid + 20} L 180 {y_bot} L {w_right} {y_bot}',
            'width': 105, 'duration': 0.6
        })

    # --- ㅍ ---
    elif cho == 'ㅍ':
        xm1 = 220 if is_vert else 330
        xm2 = 410 if is_vert else 570
        strokes.append({'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 1획 (상단 가로)',
                        'clip_box': {'x': 80 if is_vert else 140, 'y': y_top - 20, 'w': w_right + 10, 'h': 75},
                        'd': f'M 90 {y_top} L {w_right} {y_top}', 'width': 95, 'duration': 0.4})
        strokes.append({'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 2획 (좌측 세로)',
                        'clip_box': {'x': xm1 - 35, 'y': y_top + 10, 'w': 70, 'h': y_bot - y_top + 10},
                        'd': f'M {xm1} {y_top} L {xm1} {y_bot}', 'width': 95, 'duration': 0.45})
        strokes.append({'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 3획 (우측 세로)',
                        'clip_box': {'x': xm2 - 35, 'y': y_top + 10, 'w': 70, 'h': y_bot - y_top + 10},
                        'd': f'M {xm2} {y_top} L {xm2} {y_bot}', 'width': 95, 'duration': 0.45})
        strokes.append({'order': ord_num + 3, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅍ 4획 (하단 가로)',
                        'clip_box': {'x': 80 if is_vert else 140, 'y': y_bot - 35, 'w': w_right + 10, 'h': 75},
                        'd': f'M 90 {y_bot} L {w_right} {y_bot}', 'width': 95, 'duration': 0.4})

    # --- ㅎ ---
    elif cho == 'ㅎ':
        if archetype in ('V1', 'V2', 'C1', 'C2'):
            # Authentic metrics for vertical layout (한)
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 1획 (상단 꼭지점)',
                'clip_box': {'x': 270, 'y': 50, 'w': 95, 'h': 118},
                'd': 'M 319 50 L 319 168', 'width': 100, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 2획 (중간 가로획)',
                'clip_box': {'x': 45, 'y': 155, 'w': 550, 'h': 85},
                'd': 'M 45 197 L 595 197', 'width': 95, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 3획 (원형 폐곡선)',
                'clip_box': {'x': 95, 'y': 270, 'w': 450, 'h': 355},
                'd': 'M 319 312 A 177 136 0 1 0 319 584 A 177 136 0 1 0 319 312',
                'width': 115, 'duration': 0.75
            })
        else:
            cx = 460
            strokes.append({
                'order': ord_num, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 1획 (상단 꼭지점)',
                'clip_box': {'x': cx - 50, 'y': y_top - 40, 'w': 100, 'h': 65},
                'd': f'M {cx} {y_top - 40} L {cx} {y_top + 15}', 'width': 95, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 1, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 2획 (중간 가로획)',
                'clip_box': {'x': 140, 'y': y_top + 10, 'w': w_right + 10, 'h': 75},
                'd': f'M 150 {y_top + 30} L {w_right} {y_top + 30}', 'width': 95, 'duration': 0.45
            })
            cy = (y_top + 70 + y_bot) // 2
            ry = (y_bot - (y_top + 70)) // 2
            rx = ry + 25
            strokes.append({
                'order': ord_num + 2, 'part': '초성', 'color': '#3b82f6', 'name': 'ㅎ 3획 (원형 폐곡선)',
                'clip_box': {'x': cx - rx - 20, 'y': cy - ry - 20, 'w': rx * 2 + 40, 'h': ry * 2 + 40},
                'd': f'M {cx} {cy - ry} A {rx} {ry} 0 1 0 {cx} {cy + ry} A {rx} {ry} 0 1 0 {cx} {cy - ry}',
                'width': 115, 'duration': 0.75
            })

    return strokes


def get_jung_strokes(jung: str, archetype: str, start_order: int, cho: str = '') -> List[Dict[str, Any]]:
    """Generates standard stroke order trajectories for Jung (Vowels) based on archetype."""
    strokes = []
    ord_num = start_order
    is_vert = archetype in ('V1', 'V2')
    has_jong = archetype in ('V2', 'H2', 'C2')

    # --- VERTICAL VOWELS (V1, V2) ---
    if is_vert:
        y_top = 45
        stem_x = 752 if (cho in ('ㅂ', 'ㅃ', 'ㅁ', 'ㅍ') and archetype == 'V2') else (710 if has_jong else 703)
        y_bot = 740 if has_jong else 960
        b_w = 890

        if jung == 'ㅏ':
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 1획 (세로 기둥)',
                'clip_box': {'x': stem_x - 50, 'y': y_top, 'w': 100, 'h': y_bot - y_top + 15},
                'd': f'M {stem_x} {y_top} L {stem_x} {y_bot}', 'width': 105, 'duration': 0.65
            })
            if has_jong:
                b_y = 385 if cho == 'ㅎ' else (260 if cho in ('ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ') else 317)
            else:
                b_y = 454
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 2획 (우측 가로)',
                'clip_box': {'x': stem_x + 35, 'y': b_y - 45, 'w': b_w - stem_x + 10, 'h': 95},
                'd': f'M {stem_x} {b_y} L {b_w} {b_y}', 'width': 105, 'duration': 0.3
            })

        elif jung == 'ㅑ':
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅑ 1획 (세로 기둥)',
                'clip_box': {'x': stem_x - 50, 'y': y_top, 'w': 100, 'h': y_bot - y_top + 15},
                'd': f'M {stem_x} {y_top} L {stem_x} {y_bot}', 'width': 105, 'duration': 0.65
            })
            b1_y = 250 if has_jong else 350
            b2_y = 390 if has_jong else 560
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅑ 2획 (상단 가지)',
                'clip_box': {'x': stem_x + 35, 'y': b1_y - 35, 'w': b_w - stem_x + 10, 'h': 70},
                'd': f'M {stem_x} {b1_y} L {b_w} {b1_y}', 'width': 85, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅑ 3획 (하단 가지)',
                'clip_box': {'x': stem_x + 35, 'y': b2_y - 35, 'w': b_w - stem_x + 10, 'h': 70},
                'd': f'M {stem_x} {b2_y} L {b_w} {b2_y}', 'width': 85, 'duration': 0.3
            })

        elif jung == 'ㅓ':
            b_y = 317 if has_jong else 454
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 1획 (좌측 가로)',
                'clip_box': {'x': stem_x - 180, 'y': b_y - 40, 'w': 190, 'h': 80},
                'd': f'M {stem_x - 170} {b_y} L {stem_x + 15} {b_y}', 'width': 95, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 2획 (세로 기둥)',
                'clip_box': {'x': stem_x - 50, 'y': y_top, 'w': 100, 'h': y_bot - y_top + 15},
                'd': f'M {stem_x} {y_top} L {stem_x} {y_bot}', 'width': 105, 'duration': 0.65
            })

        elif jung == 'ㅕ':
            b1_y = 214 if has_jong else 350
            b2_y = 378 if has_jong else 560
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 1획 (상단 가로)',
                'clip_box': {'x': stem_x - 250, 'y': b1_y - 35, 'w': 260, 'h': 70},
                'd': f'M {stem_x - 240} {b1_y} L {stem_x + 15} {b1_y}', 'width': 85, 'duration': 0.32
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 2획 (하단 가로)',
                'clip_box': {'x': stem_x - 250, 'y': b2_y - 35, 'w': 260, 'h': 70},
                'd': f'M {stem_x - 240} {b2_y} L {stem_x + 15} {b2_y}', 'width': 85, 'duration': 0.32
            })
            y_bot_stem = 535 if (cho == 'ㅂ' and has_jong) else y_bot
            strokes.append({
                'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅕ 3획 (세로 기둥)',
                'clip_box': {'x': stem_x - 50, 'y': y_top, 'w': 100, 'h': y_bot_stem - y_top + 15},
                'd': f'M {stem_x} {y_top} L {stem_x} {y_bot_stem}', 'width': 100, 'duration': 0.55
            })

        elif jung == 'ㅣ':
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅣ (세로 기둥)',
                'clip_box': {'x': stem_x - 50, 'y': y_top, 'w': 100, 'h': y_bot - y_top + 15},
                'd': f'M {stem_x} {y_top} L {stem_x} {y_bot}', 'width': 105, 'duration': 0.65
            })

        elif jung in ('ㅐ', 'ㅔ'):
            s1_x = stem_x - 90
            s2_x = stem_x + 70
            b_y = 317 if has_jong else 454
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': f'{jung} 1획 (첫째 기둥)',
                'clip_box': {'x': s1_x - 40, 'y': y_top, 'w': 80, 'h': y_bot - y_top + 15},
                'd': f'M {s1_x} {y_top} L {s1_x} {y_bot}', 'width': 95, 'duration': 0.55
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': f'{jung} 2획 (연결 가로)',
                'clip_box': {'x': s1_x + 20, 'y': b_y - 35, 'w': s2_x - s1_x - 10, 'h': 70},
                'd': f'M {s1_x} {b_y} L {s2_x} {b_y}', 'width': 85, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': f'{jung} 3획 (둘째 기둥)',
                'clip_box': {'x': s2_x - 40, 'y': y_top, 'w': 85, 'h': y_bot - y_top + 15},
                'd': f'M {s2_x} {y_top} L {s2_x} {y_bot}', 'width': 95, 'duration': 0.55
            })

        elif jung in ('ㅒ', 'ㅖ'):
            s1_x = stem_x - 90
            s2_x = stem_x + 70
            b1_y = 250 if has_jong else 350
            b2_y = 390 if has_jong else 560
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': f'{jung} 1획 (첫째 기둥)',
                'clip_box': {'x': s1_x - 40, 'y': y_top, 'w': 80, 'h': y_bot - y_top + 15},
                'd': f'M {s1_x} {y_top} L {s1_x} {y_bot}', 'width': 95, 'duration': 0.55
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': f'{jung} 2획 (상단 가지)',
                'clip_box': {'x': s1_x + 20, 'y': b1_y - 35, 'w': s2_x - s1_x - 10, 'h': 70},
                'd': f'M {s1_x} {b1_y} L {s2_x} {b1_y}', 'width': 80, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': f'{jung} 3획 (하단 가지)',
                'clip_box': {'x': s1_x + 20, 'y': b2_y - 35, 'w': s2_x - s1_x - 10, 'h': 70},
                'd': f'M {s1_x} {b2_y} L {s2_x} {b2_y}', 'width': 80, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 3, 'part': '중성', 'color': '#f59e0b', 'name': f'{jung} 4획 (둘째 기둥)',
                'clip_box': {'x': s2_x - 40, 'y': y_top, 'w': 85, 'h': y_bot - y_top + 15},
                'd': f'M {s2_x} {y_top} L {s2_x} {y_bot}', 'width': 95, 'duration': 0.55
            })

    # --- HORIZONTAL VOWELS (H1, H2) ---
    elif archetype in ('H1', 'H2'):
        if jung == 'ㅡ':
            bar_y = 615 if archetype == 'H1' else 423
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅡ (긴 가로선)',
                'clip_box': {'x': 40, 'y': bar_y - 45, 'w': 840, 'h': 90},
                'd': f'M 40 {bar_y} L 880 {bar_y}', 'width': 100, 'duration': 0.5
            })

        elif jung == 'ㅗ':
            if archetype == 'H1':
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                    'clip_box': {'x': 355, 'y': 430, 'w': 110, 'h': 345},
                    'd': 'M 409 430 L 409 775', 'width': 105, 'duration': 0.35
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가로선)',
                    'clip_box': {'x': 40, 'y': 750, 'w': 835, 'h': 95},
                    'd': 'M 40 796 L 875 796', 'width': 95, 'duration': 0.5
                })
            else: # H2 (곡, 꽃)
                stub_x = 476 if cho in ('ㄲ', 'ㅃ', 'ㅉ') else 427
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                    'clip_box': {'x': stub_x - 60, 'y': 280, 'w': 120, 'h': 210},
                    'd': f'M {stub_x} 280 L {stub_x} 490', 'width': 105, 'duration': 0.3
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
                'clip_box': {'x': 40, 'y': bar_y - 45, 'w': 835, 'h': 95},
                'd': f'M 40 {bar_y} L 875 {bar_y}', 'width': 100, 'duration': 0.5
            })

        elif jung == 'ㅜ':
            bar_y = 442
            p_y2 = 820 if archetype == 'H1' else 632
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가로선)',
                'clip_box': {'x': 40, 'y': bar_y - 40, 'w': 840, 'h': 80},
                'd': f'M 46 {bar_y} L 875 {bar_y}', 'width': 90, 'duration': 0.5
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                'clip_box': {'x': 410, 'y': bar_y + 10, 'w': 100, 'h': p_y2 - bar_y + 20},
                'd': f'M 457 {bar_y} L 457 {p_y2}', 'width': 95, 'duration': 0.3
            })

        elif jung == 'ㅠ':
            bar_y = 442
            p_y2 = 820 if archetype == 'H1' else 632
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅠ 1획 (가로선)',
                'clip_box': {'x': 40, 'y': bar_y - 40, 'w': 840, 'h': 80},
                'd': f'M 46 {bar_y} L 875 {bar_y}', 'width': 90, 'duration': 0.5
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅠ 2획 (좌세로점)',
                'clip_box': {'x': 320, 'y': bar_y + 10, 'w': 90, 'h': p_y2 - bar_y + 20},
                'd': f'M 365 {bar_y} L 365 {p_y2}', 'width': 85, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅠ 3획 (우세로점)',
                'clip_box': {'x': 540, 'y': bar_y + 10, 'w': 90, 'h': p_y2 - bar_y + 20},
                'd': f'M 585 {bar_y} L 585 {p_y2}', 'width': 85, 'duration': 0.3
            })

    # --- COMPOUND VOWELS (C1, C2) ---
    else:
        # e.g. ㅘ, ㅙ, ㅚ, ㅝ, ㅞ, ㅟ, ㅢ
        is_c1 = (archetype == 'C1')
        h_part = 'ㅗ' if jung in ('ㅘ','ㅙ','ㅚ') else ('ㅜ' if jung in ('ㅝ','ㅞ','ㅟ') else 'ㅡ')
        v_part = 'ㅏ' if jung == 'ㅘ' else ('ㅓ' if jung == 'ㅝ' else ('ㅐ' if jung == 'ㅙ' else ('ㅔ' if jung == 'ㅞ' else 'ㅣ')))

        # 1. Horizontal component
        if h_part == 'ㅗ':
            if is_c1:
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                    'clip_box': {'x': 215, 'y': 400, 'w': 120, 'h': 295},
                    'd': 'M 273 400 L 273 695', 'width': 100, 'duration': 0.35
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가로선)',
                    'clip_box': {'x': 35, 'y': 655, 'w': 585, 'h': 115},
                    'd': 'M 35 712 L 615 712', 'width': 100, 'duration': 0.5
                })
            else: # C2 (광)
                strokes.append({
                    'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 1획 (세로점)',
                    'clip_box': {'x': 215, 'y': 300, 'w': 120, 'h': 200},
                    'd': 'M 276 300 L 276 495', 'width': 100, 'duration': 0.3
                })
                strokes.append({
                    'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅗ 2획 (가로선)',
                    'clip_box': {'x': 35, 'y': 450, 'w': 590, 'h': 120},
                    'd': 'M 35 508 L 620 508', 'width': 100, 'duration': 0.45
                })
            ord_num += 2
        elif h_part == 'ㅜ':
            y_bar = 645 if is_c1 else 465
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 1획 (가로선)',
                'clip_box': {'x': 35, 'y': y_bar - 45, 'w': 585, 'h': 100},
                'd': f'M 35 {y_bar} L 615 {y_bar}', 'width': 100, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅜ 2획 (세로점)',
                'clip_box': {'x': 215, 'y': y_bar, 'w': 120, 'h': 240 if is_c1 else 170},
                'd': f'M 273 {y_bar} L 273 {y_bar + (230 if is_c1 else 160)}', 'width': 100, 'duration': 0.3
            })
            ord_num += 2
        else: # ㅡ
            y_bar = 705 if is_c1 else 508
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅡ (가로선)',
                'clip_box': {'x': 35, 'y': y_bar - 50, 'w': 620, 'h': 110},
                'd': f'M 35 {y_bar} L 650 {y_bar}', 'width': 100, 'duration': 0.5
            })
            ord_num += 1

        # 2. Vertical component
        stem_x = 702 if is_c1 else 712
        y_bot_v = 960 if is_c1 else 625
        h_v = y_bot_v - 45 + 15
        if v_part == 'ㅏ':
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 1획 (세로기둥)',
                'clip_box': {'x': stem_x - 50, 'y': 45, 'w': 105, 'h': h_v},
                'd': f'M {stem_x} 45 L {stem_x} {y_bot_v}', 'width': 105, 'duration': 0.6
            })
            by = 466 if is_c1 else 334
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅏ 2획 (가로가지)',
                'clip_box': {'x': stem_x + 30, 'y': by - 45, 'w': 165, 'h': 95},
                'd': f'M {stem_x} {by} L 895 {by}', 'width': 95, 'duration': 0.3
            })
        elif v_part == 'ㅓ':
            by = 466 if is_c1 else 334
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 1획 (가로가지)',
                'clip_box': {'x': stem_x - 180, 'y': by - 45, 'w': 190, 'h': 95},
                'd': f'M {stem_x - 170} {by} L {stem_x + 15} {by}', 'width': 95, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅓ 2획 (세로기둥)',
                'clip_box': {'x': stem_x - 50, 'y': 45, 'w': 105, 'h': h_v},
                'd': f'M {stem_x} 45 L {stem_x} {y_bot_v}', 'width': 105, 'duration': 0.6
            })
        elif v_part == 'ㅣ':
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': 'ㅣ (세로기둥)',
                'clip_box': {'x': stem_x - 45, 'y': 45, 'w': 105, 'h': h_v},
                'd': f'M {stem_x} 45 L {stem_x} {y_bot_v}', 'width': 105, 'duration': 0.65
            })
        else: # ㅐ, ㅔ
            s1 = stem_x - 80
            s2 = stem_x + 60
            by = 466 if is_c1 else 334
            strokes.append({
                'order': ord_num, 'part': '중성', 'color': '#f59e0b', 'name': f'{v_part} 1획 (첫기둥)',
                'clip_box': {'x': s1 - 40, 'y': 45, 'w': 80, 'h': h_v},
                'd': f'M {s1} 45 L {s1} {y_bot_v}', 'width': 95, 'duration': 0.55
            })
            strokes.append({
                'order': ord_num + 1, 'part': '중성', 'color': '#f59e0b', 'name': f'{v_part} 2획 (가지)',
                'clip_box': {'x': s1 + 10, 'y': by - 40, 'w': s2 - s1, 'h': 80},
                'd': f'M {s1} {by} L {s2} {by}', 'width': 85, 'duration': 0.3
            })
            strokes.append({
                'order': ord_num + 2, 'part': '중성', 'color': '#f59e0b', 'name': f'{v_part} 3획 (둘째기둥)',
                'clip_box': {'x': s2 - 40, 'y': 45, 'w': 85, 'h': h_v},
                'd': f'M {s2} 45 L {s2} {y_bot_v}', 'width': 95, 'duration': 0.55
            })

    return strokes


def get_jong_strokes(jong: str, start_order: int, archetype: str = 'H2') -> List[Dict[str, Any]]:
    """Generates standard stroke order trajectories for Jong (Final Consonants / Batchim)."""
    strokes = []
    ord_num = start_order

    # --- ㄱ ---
    if jong == 'ㄱ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㄱ 받침 (직각 꺾음)',
            'clip_box': {'x': 130, 'y': 615, 'w': 645, 'h': 355},
            'd': 'M 130 675 L 725 675 L 725 965', 'width': 125, 'duration': 0.65
        })

    # --- ㄲ ---
    elif jong == 'ㄲ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': '첫째 ㄱ 받침',
            'clip_box': {'x': 130, 'y': 615, 'w': 310, 'h': 355},
            'd': 'M 130 660 L 410 660 L 410 965', 'width': 105, 'duration': 0.5
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': '둘째 ㄱ 받침',
            'clip_box': {'x': 450, 'y': 615, 'w': 330, 'h': 355},
            'd': 'M 450 660 L 740 660 L 740 965', 'width': 105, 'duration': 0.5
        })

    # --- ㄴ ---
    elif jong == 'ㄴ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㄴ 받침 (세로-가로 꺾음)',
            'clip_box': {'x': 180, 'y': 670, 'w': 620, 'h': 275},
            'd': 'M 230 670 L 230 904 L 800 904', 'width': 105, 'duration': 0.65
        })

    # --- ㄷ ---
    elif jong == 'ㄷ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㄷ 1획 (상단 가로)',
            'clip_box': {'x': 180, 'y': 635, 'w': 620, 'h': 75},
            'd': 'M 190 665 L 780 665', 'width': 95, 'duration': 0.4
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㄷ 2획 (하단 ㄴ 꺾음)',
            'clip_box': {'x': 180, 'y': 685, 'w': 620, 'h': 260},
            'd': 'M 240 680 L 240 905 L 780 905', 'width': 105, 'duration': 0.6
        })

    # --- ㄹ ---
    elif jong == 'ㄹ':
        # Handles both wide V2 (별) and centered H2 (글)
        x_stem = 254 if archetype == 'V2' else 190
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㄹ 1획 (상단 ㄱ)',
            'clip_box': {'x': 130, 'y': 530, 'w': 720, 'h': 200},
            'd': f'M {x_stem - 50} 602 L 755 602 L 752 730', 'width': 125, 'duration': 0.6
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㄹ 2획 (중간 가로)',
            'clip_box': {'x': 130, 'y': 700, 'w': 720, 'h': 85},
            'd': f'M {x_stem - 50} 750 L 805 750', 'width': 105, 'duration': 0.45
        })
        strokes.append({
            'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㄹ 3획 (하단 ㄴ)',
            'clip_box': {'x': 130, 'y': 760, 'w': 720, 'h': 200},
            'd': f'M {x_stem} 750 L {x_stem} 914 L 835 914', 'width': 115, 'duration': 0.65
        })

    # --- ㅁ ---
    elif jong == 'ㅁ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅁ 1획 (좌측 세로)',
            'clip_box': {'x': 148, 'y': 624, 'w': 89, 'h': 325},
            'd': 'M 192 624 L 192 949', 'width': 95, 'duration': 0.45
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅁ 2획 (상우 꺾음)',
            'clip_box': {'x': 233, 'y': 624, 'w': 536, 'h': 325},
            'd': 'M 192 661 L 724 661 L 724 949', 'width': 95, 'duration': 0.6
        })
        strokes.append({
            'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㅁ 3획 (하단 가로)',
            'clip_box': {'x': 233, 'y': 874, 'w': 454, 'h': 75},
            'd': 'M 192 911 L 724 911', 'width': 85, 'duration': 0.4
        })

    # --- ㅂ ---
    elif jong == 'ㅂ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅂ 1획 (좌측 세로)',
            'clip_box': {'x': 150, 'y': 580, 'w': 100, 'h': 370},
            'd': 'M 190 580 L 190 950', 'width': 95, 'duration': 0.45
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅂ 2획 (우측 세로)',
            'clip_box': {'x': 680, 'y': 580, 'w': 100, 'h': 370},
            'd': 'M 720 580 L 720 950', 'width': 95, 'duration': 0.45
        })
        strokes.append({
            'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㅂ 3획 (중간 가로)',
            'clip_box': {'x': 240, 'y': 710, 'w': 450, 'h': 75},
            'd': 'M 190 745 L 720 745', 'width': 85, 'duration': 0.35
        })
        strokes.append({
            'order': ord_num + 3, 'part': '종성', 'color': '#a855f7', 'name': 'ㅂ 4획 (하단 가로)',
            'clip_box': {'x': 240, 'y': 880, 'w': 450, 'h': 75},
            'd': 'M 190 910 L 720 910', 'width': 85, 'duration': 0.35
        })

    # --- ㅅ ---
    elif jong == 'ㅅ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅅ 1획 (좌측 빗침)',
            'clip_box': {'x': 130, 'y': 620, 'w': 340, 'h': 335},
            'd': 'M 460 620 L 150 940', 'width': 105, 'duration': 0.55
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅅ 2획 (우측 빗침)',
            'clip_box': {'x': 440, 'y': 620, 'w': 340, 'h': 335},
            'd': 'M 440 700 L 770 940', 'width': 105, 'duration': 0.55
        })

    # --- ㅆ ---
    elif jong == 'ㅆ':
        for idx, ox in enumerate([0, 310]):
            cx = 280 + ox
            pfx = '첫째 ' if idx == 0 else '둘째 '
            o = ord_num + idx * 2
            strokes.append({'order': o, 'part': '종성', 'color': '#a855f7', 'name': pfx + 'ㅅ 1획',
                            'clip_box': {'x': cx - 140, 'y': 620, 'w': 150, 'h': 335},
                            'd': f'M {cx} 620 L {cx - 130} 940', 'width': 95, 'duration': 0.5})
            strokes.append({'order': o + 1, 'part': '종성', 'color': '#a855f7', 'name': pfx + 'ㅅ 2획',
                            'clip_box': {'x': cx - 15, 'y': 620, 'w': 150, 'h': 335},
                            'd': f'M {cx - 15} 690 L {cx + 120} 940', 'width': 95, 'duration': 0.5})

    # --- ㅇ ---
    elif jong == 'ㅇ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅇ 받침 (원형 폐곡선)',
            'clip_box': {'x': 140, 'y': 615, 'w': 645, 'h': 355},
            'd': 'M 462 662 A 258 130 0 1 0 462 922 A 258 130 0 1 0 462 662',
            'width': 120, 'duration': 0.75
        })

    # --- ㅈ ---
    elif jong == 'ㅈ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅈ 1획 (가로선)',
            'clip_box': {'x': 150, 'y': 615, 'w': 620, 'h': 75},
            'd': 'M 160 650 L 760 650', 'width': 95, 'duration': 0.45
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅈ 2획 (좌측 빗침)',
            'clip_box': {'x': 120, 'y': 650, 'w': 360, 'h': 305},
            'd': 'M 460 650 L 140 940', 'width': 100, 'duration': 0.55
        })
        strokes.append({
            'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㅈ 3획 (우측 빗침)',
            'clip_box': {'x': 440, 'y': 650, 'w': 360, 'h': 305},
            'd': 'M 440 730 L 780 940', 'width': 100, 'duration': 0.55
        })

    # --- ㅊ ---
    elif jong == 'ㅊ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅊ 1획 (상단 꼭지)',
            'clip_box': {'x': 405, 'y': 530, 'w': 105, 'h': 110},
            'd': 'M 458 530 L 458 640', 'width': 100, 'duration': 0.28
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅊ 2획 (가로선)',
            'clip_box': {'x': 145, 'y': 625, 'w': 625, 'h': 80},
            'd': 'M 145 665 L 770 665', 'width': 95, 'duration': 0.45
        })
        strokes.append({
            'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㅊ 3획 (좌측 곡선 빗침)',
            'clip_box': {'x': 110, 'y': 690, 'w': 355, 'h': 275},
            'd': 'M 465 690 C 400 780, 270 860, 125 935', 'width': 180, 'duration': 0.55
        })
        strokes.append({
            'order': ord_num + 3, 'part': '종성', 'color': '#a855f7', 'name': 'ㅊ 4획 (우측 곡선 빗침)',
            'clip_box': {'x': 450, 'y': 690, 'w': 360, 'h': 275},
            'd': 'M 450 690 C 515 780, 645 860, 790 935', 'width': 180, 'duration': 0.55
        })

    # --- ㅋ ---
    elif jong == 'ㅋ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅋ 1획 (ㄱ 꺾음)',
            'clip_box': {'x': 130, 'y': 620, 'w': 645, 'h': 350},
            'd': 'M 130 687 L 725 687 L 725 965', 'width': 115, 'duration': 0.65
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅋ 2획 (중간 가로)',
            'clip_box': {'x': 155, 'y': 780, 'w': 560, 'h': 75},
            'd': 'M 165 810 L 700 810', 'width': 90, 'duration': 0.4
        })

    # --- ㅌ ---
    elif jong == 'ㅌ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅌ 1획 (상단 가로)',
            'clip_box': {'x': 180, 'y': 625, 'w': 620, 'h': 70},
            'd': 'M 190 655 L 780 655', 'width': 95, 'duration': 0.4
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅌ 2획 (중간 가로)',
            'clip_box': {'x': 180, 'y': 750, 'w': 620, 'h': 70},
            'd': 'M 190 780 L 780 780', 'width': 90, 'duration': 0.4
        })
        strokes.append({
            'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㅌ 3획 (하단 ㄴ 꺾음)',
            'clip_box': {'x': 180, 'y': 790, 'w': 620, 'h': 170},
            'd': 'M 240 760 L 240 910 L 780 910', 'width': 105, 'duration': 0.6
        })

    # --- ㅍ ---
    elif jong == 'ㅍ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅍ 1획 (상단 가로)',
            'clip_box': {'x': 160, 'y': 625, 'w': 640, 'h': 70},
            'd': 'M 170 655 L 790 655', 'width': 95, 'duration': 0.4
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅍ 2획 (좌측 세로)',
            'clip_box': {'x': 280, 'y': 650, 'w': 75, 'h': 270},
            'd': 'M 315 655 L 315 915', 'width': 95, 'duration': 0.45
        })
        strokes.append({
            'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㅍ 3획 (우측 세로)',
            'clip_box': {'x': 600, 'y': 650, 'w': 75, 'h': 270},
            'd': 'M 640 655 L 640 915', 'width': 95, 'duration': 0.45
        })
        strokes.append({
            'order': ord_num + 3, 'part': '종성', 'color': '#a855f7', 'name': 'ㅍ 4획 (하단 가로)',
            'clip_box': {'x': 160, 'y': 880, 'w': 640, 'h': 70},
            'd': 'M 170 910 L 790 910', 'width': 95, 'duration': 0.4
        })

    # --- ㅎ ---
    elif jong == 'ㅎ':
        strokes.append({
            'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': 'ㅎ 1획 (상단 꼭지)',
            'clip_box': {'x': 405, 'y': 550, 'w': 105, 'h': 85},
            'd': 'M 458 550 L 458 630', 'width': 95, 'duration': 0.28
        })
        strokes.append({
            'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': 'ㅎ 2획 (가로선)',
            'clip_box': {'x': 145, 'y': 620, 'w': 625, 'h': 80},
            'd': 'M 155 655 L 760 655', 'width': 95, 'duration': 0.45
        })
        strokes.append({
            'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': 'ㅎ 3획 (원형 폐곡선)',
            'clip_box': {'x': 270, 'y': 680, 'w': 380, 'h': 270},
            'd': 'M 460 705 A 150 100 0 1 0 460 905 A 150 100 0 1 0 460 705',
            'width': 110, 'duration': 0.75
        })

    # --- 겹받침 (11종) ---
    else:
        parts = {
            'ㄳ': ('ㄱ', 'ㅅ'), 'ㄵ': ('ㄴ', 'ㅈ'), 'ㄶ': ('ㄴ', 'ㅎ'),
            'ㄺ': ('ㄹ', 'ㄱ'), 'ㄻ': ('ㄹ', 'ㅁ'), 'ㄼ': ('ㄹ', 'ㅂ'),
            'ㄽ': ('ㄹ', 'ㅅ'), 'ㄾ': ('ㄹ', 'ㅌ'), 'ㄿ': ('ㄹ', 'ㅍ'),
            'ㅀ': ('ㄹ', 'ㅎ'), 'ㅄ': ('ㅂ', 'ㅅ')
        }.get(jong, ('ㄱ', 'ㄱ'))

        p1, p2 = parts[0], parts[1]

        # 1. Left batchim (x in [130, 480])
        if p1 == 'ㄹ':
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} 1획 (좌측 ㄹ 상단 ㄱ)',
                'clip_box': {'x': 130, 'y': 565, 'w': 320, 'h': 175},
                'd': 'M 140 611 L 445 611 L 445 727', 'width': 105, 'duration': 0.5
            })
            strokes.append({
                'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} 2획 (좌측 ㄹ 중간 가로)',
                'clip_box': {'x': 130, 'y': 715, 'w': 320, 'h': 85},
                'd': 'M 140 757 L 445 757', 'width': 95, 'duration': 0.4
            })
            strokes.append({
                'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} 3획 (좌측 ㄹ 하단 ㄴ)',
                'clip_box': {'x': 130, 'y': 780, 'w': 385, 'h': 180},
                'd': 'M 182 780 L 182 914 L 515 914', 'width': 105, 'duration': 0.55
            })
            ord_num += 3
        elif p1 == 'ㄴ':
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} 1획 (좌측 ㄴ)',
                'clip_box': {'x': 130, 'y': 660, 'w': 350, 'h': 295},
                'd': 'M 180 660 L 180 914 L 460 914', 'width': 105, 'duration': 0.6
            })
            ord_num += 1
        elif p1 == 'ㅂ':
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} 1획 (좌측 ㅂ)',
                'clip_box': {'x': 130, 'y': 580, 'w': 350, 'h': 370},
                'd': 'M 170 580 L 170 940 L 440 940 L 440 580', 'width': 100, 'duration': 0.65
            })
            ord_num += 1
        else: # ㄱ
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} 1획 (좌측 ㄱ)',
                'clip_box': {'x': 130, 'y': 600, 'w': 340, 'h': 355},
                'd': 'M 140 640 L 430 640 L 430 940', 'width': 105, 'duration': 0.55
            })
            ord_num += 1

        # 2. Right batchim (x in [460, 830])
        if p2 == 'ㄱ':
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num}획 (우측 ㄱ)',
                'clip_box': {'x': 465, 'y': 565, 'w': 300, 'h': 395},
                'd': 'M 470 612 L 711 612 L 711 960', 'width': 105, 'duration': 0.55
            })
        elif p2 == 'ㅅ':
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num}획 (우측 ㅅ 1획)',
                'clip_box': {'x': 465, 'y': 610, 'w': 180, 'h': 345},
                'd': 'M 640 610 L 480 940', 'width': 95, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num+1}획 (우측 ㅅ 2획)',
                'clip_box': {'x': 620, 'y': 610, 'w': 180, 'h': 345},
                'd': 'M 625 680 L 780 940', 'width': 95, 'duration': 0.45
            })
        elif p2 == 'ㅈ':
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num}획 (우측 ㅈ 1획)',
                'clip_box': {'x': 470, 'y': 610, 'w': 310, 'h': 65},
                'd': 'M 480 640 L 770 640', 'width': 90, 'duration': 0.35
            })
            strokes.append({
                'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num+1}획 (우측 ㅈ 2획)',
                'clip_box': {'x': 470, 'y': 640, 'w': 320, 'h': 310},
                'd': 'M 625 640 L 480 940', 'width': 95, 'duration': 0.45
            })
            strokes.append({
                'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num+2}획 (우측 ㅈ 3획)',
                'clip_box': {'x': 610, 'y': 670, 'w': 180, 'h': 280},
                'd': 'M 610 710 L 780 940', 'width': 95, 'duration': 0.45
            })
        elif p2 == 'ㅎ':
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num}획 (우측 ㅎ 1획)',
                'clip_box': {'x': 570, 'y': 560, 'w': 80, 'h': 65},
                'd': 'M 610 560 L 610 620', 'width': 85, 'duration': 0.25
            })
            strokes.append({
                'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num+1}획 (우측 ㅎ 2획)',
                'clip_box': {'x': 470, 'y': 615, 'w': 290, 'h': 75},
                'd': 'M 480 645 L 750 645', 'width': 85, 'duration': 0.35
            })
            strokes.append({
                'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num+2}획 (우측 ㅎ 3획)',
                'clip_box': {'x': 480, 'y': 680, 'w': 280, 'h': 270},
                'd': 'M 615 700 A 100 80 0 1 0 615 890 A 100 80 0 1 0 615 700', 'width': 95, 'duration': 0.6
            })
        elif p2 == 'ㅁ':
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num}획 (우측 ㅁ)',
                'clip_box': {'x': 470, 'y': 610, 'w': 310, 'h': 345},
                'd': 'M 500 620 L 500 930 L 760 930 L 760 620 L 500 620', 'width': 95, 'duration': 0.65
            })
        elif p2 == 'ㅂ':
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num}획 (우측 ㅂ)',
                'clip_box': {'x': 470, 'y': 580, 'w': 310, 'h': 370},
                'd': 'M 500 580 L 500 940 L 760 940 L 760 580', 'width': 95, 'duration': 0.65
            })
        elif p2 == 'ㅌ':
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num}획 (우측 ㅌ 1획)',
                'clip_box': {'x': 470, 'y': 610, 'w': 310, 'h': 65},
                'd': 'M 480 635 L 770 635', 'width': 85, 'duration': 0.35
            })
            strokes.append({
                'order': ord_num + 1, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num+1}획 (우측 ㅌ 2획)',
                'clip_box': {'x': 470, 'y': 710, 'w': 310, 'h': 65},
                'd': 'M 480 735 L 770 735', 'width': 85, 'duration': 0.35
            })
            strokes.append({
                'order': ord_num + 2, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num+2}획 (우측 ㅌ 3획)',
                'clip_box': {'x': 470, 'y': 740, 'w': 310, 'h': 210},
                'd': 'M 515 720 L 515 910 L 770 910', 'width': 95, 'duration': 0.55
            })
        elif p2 == 'ㅍ':
            strokes.append({
                'order': ord_num, 'part': '종성', 'color': '#a855f7', 'name': f'{jong} {ord_num}획 (우측 ㅍ)',
                'clip_box': {'x': 470, 'y': 610, 'w': 310, 'h': 345},
                'd': 'M 480 635 L 770 635 M 540 635 L 540 910 M 710 635 L 710 910 M 480 910 L 770 910',
                'width': 90, 'duration': 0.65
            })

    return strokes
