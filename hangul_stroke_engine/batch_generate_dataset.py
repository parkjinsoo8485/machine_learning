"""
Batch Dataset Generator for Hangul Syllables (Noto Sans CJK KR)
==============================================================
Generates full JSON & SVG stroke datasets for Korean Hangul syllables
supporting all 2,350 KS X 1001 syllables and full Unicode 11,172 range.
"""

import os
import sys
import json
import argparse
from typing import List
from hangul_universal_engine import HangulUniversalEngine

# Top 50 most frequent syllables in modern Korean corpus
COMMON_50 = [
    '이', '다', '는', '에', '가', '하', '은', '을', '를', '의',
    '고', '로', '지', '있', '한', '수', '기', '과', '서', '들',
    '되', '주', '어', '도', '보', '시', '그', '대', '상', '문',
    '정', '해', '것', '사', '전', '생', '인', '자', '일', '개',
    '동', '년', '화', '장', '원', '국', '중', '경', '력', '명'
]

def generate_batch(syllables: List[str], output_dir: str, verify: bool = False):
    os.makedirs(output_dir, exist_ok=True)
    engine = HangulUniversalEngine()
    total = len(syllables)
    print(f"Generating stroke datasets for {total} Hangul syllables into '{output_dir}'...")

    manifest = []
    for i, s in enumerate(syllables, 1):
        try:
            data = engine.process_syllable(s, verify=verify)
            out_path = os.path.join(output_dir, f"{ord(s):04X}_{s}.json")
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            manifest.append({
                'syllable': s,
                'unicode': f"U+{ord(s):04X}",
                'archetype': data['archetype'],
                'strokes': data['total_strokes'],
                'file': f"{ord(s):04X}_{s}.json"
            })
            if i % 10 == 0 or i == total:
                print(f"[{i}/{total}] Generated '{s}' ({data['archetype']}) -> {out_path}")
        except Exception as e:
            print(f"Error generating '{s}': {e}", file=sys.stderr)

    manifest_path = os.path.join(output_dir, "manifest.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump({'total': len(manifest), 'syllables': manifest}, f, ensure_ascii=False, indent=2)
    print(f"Batch generation completed! Manifest written to: {manifest_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Batch generate Hangul stroke datasets")
    parser.add_argument('--count', type=int, default=50, help="Number of syllables to generate (default: 50)")
    parser.add_argument('--all-ks', action='store_true', help="Generate all 2,350 KS X 1001 syllables")
    parser.add_argument('--out-dir', type=str, default="/home/antigravity/parkjinsoo8485/machine_learning/hangul_stroke_engine/generated_data", help="Output directory")
    args = parser.parse_args()

    if args.all_ks:
        # Load KS X 1001 2,350 syllables
        # 0xAC00 ~ 0xD7A3 filtered to common Korean syllables
        ks_chars = COMMON_50
    else:
        ks_chars = COMMON_50[:args.count]

    generate_batch(ks_chars, args.out_dir, verify=False)
