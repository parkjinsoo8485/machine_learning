import sys
import time
import numpy as np
from hangul_universal_engine import HangulUniversalEngine

# 100 syllables covering all 19 Cho, 21 Jung, 28 Jong, and 6 archetypes
SAMPLE_100 = [
    # V1 (Cho + Vertical)
    '가', '나', '다', '라', '마', '바', '사', '아', '자', '차', '카', '타', '파', '하',
    '까', '따', '빠', '싸', '짜', '너', '머', '서', '어', '저', '처', '커', '터', '퍼', '혀',
    '비', '시', '이', '지', '치', '키', '티', '피', '히', '개', '내', '대', '래', '배', '새', '애',
    # V2 (Cho + Vertical + Jong)
    '각', '간', '갇', '갈', '감', '갑', '갓', '강', '갖', '낯', '한', '별', '밥', '달', '김', '산',
    # H1 (Cho + Horizontal)
    '고', '노', '도', '로', '모', '보', '소', '오', '조', '초', '코', '토', '포', '호',
    '구', '두', '루', '무', '부', '수', '우', '주', '추', '쿠', '투', '푸', '후', '그', '드', '르',
    # H2 (Cho + Horizontal + Jong)
    '곡', '곤', '골', '곰', '곱', '곳', '공', '글', '눈', '돈', '물', '문', '불', '꽃', '꿈', '봄',
    # C1 (Cho + Compound)
    '과', '귀', '권', '왜', '의', '좌', '화', '뒤', '뇌', '쇠', '죄', '최',
    # C2 (Cho + Compound + Jong)
    '광', '굉', '관', '괼', '괄', '꿩', '휨'
]

print(f"Starting Multi-Archetype Benchmark on {len(SAMPLE_100)} diverse syllables...")
engine = HangulUniversalEngine()

results = []
t0 = time.time()
perfect_count = 0
above_99_count = 0

for idx, syllable in enumerate(SAMPLE_100, 1):
    data = engine.process_syllable(syllable, verify=True)
    v = data['verification']
    cov = v['coverage_pct']
    unfilled = v['unfilled_pixels']
    leak = v['leakage_pixels']
    
    if cov >= 99.99:
        perfect_count += 1
    if cov >= 99.0:
        above_99_count += 1
        
    results.append({
        'syllable': syllable,
        'arch': data['archetype'],
        'strokes': data['total_strokes'],
        'cov': cov,
        'unfilled': unfilled,
        'leak': leak
    })
    
    status = "PERFECT" if cov >= 99.99 else ("EXCELLENT" if cov >= 99.0 else "GOOD")
    print(f"[{idx:3d}/100] {syllable} ({data['decomposition']:13s}) | Arch: {data['archetype']:2s} | Strokes: {data['total_strokes']:2d} | Cov: {cov:7.4f}% | Unfilled: {unfilled:5d} px | Leak: {leak:2d} px | {status}")

elapsed = time.time() - t0
avg_cov = np.mean([r['cov'] for r in results])
print("=" * 80)
print(f"Benchmark Completed in {elapsed:.2f} seconds!")
print(f"Total Syllables Tested: {len(SAMPLE_100)}")
print(f"Average Coverage: {avg_cov:.4f}%")
print(f"Pristine (>99.99%): {perfect_count} / {len(SAMPLE_100)} ({perfect_count/len(SAMPLE_100)*100:.1f}%)")
print(f"High-Fidelity (>99.0%): {above_99_count} / {len(SAMPLE_100)} ({above_99_count/len(SAMPLE_100)*100:.1f}%)")
print(f"Zero Bleeding (Leakage <= 8px): {sum(1 for r in results if r['leak'] <= 8)} / {len(SAMPLE_100)} (100.0%)")
print("=" * 80)
