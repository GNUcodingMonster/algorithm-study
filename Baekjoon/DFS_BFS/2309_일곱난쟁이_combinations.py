"""
* 문제: 백준 2309번 (일곱 난쟁이)
* 분류: 브루트포스 알고리즘, 정렬
* 풀이: itertools.combinations 및 리스트 컴프리헨션 활용
* 시간 복잡도: O(1) (N=9로 고정되어 있으므로 상수 시간)

[핵심 로직]
1. 9명 중 7명을 뽑는 조합(9C7) 대신, 가짜 난쟁이 2명을 뽑는 조합(9C2)으로 발상의 전환.
2. 전체 합에서 2명의 키를 뺐을 때 100이 되는 가짜 난쟁이 쌍을 찾음.
3. 리스트 컴프리헨션을 사용하여 원본 배열에서 가짜 난쟁이를 O(N)으로 필터링.
"""

import sys
from itertools import combinations

def solve():
    input = sys.stdin.readline
    
    # 1. 9명의 난쟁이 키 입력 및 오름차순 정렬
    dwarfs = [int(input()) for _ in range(9)]
    dwarfs.sort()
    
    total_sum = sum(dwarfs)
    
    # 2. 9명 중 가짜 난쟁이 2명을 뽑는 모든 조합 탐색 (9C2 = 36번)
    for fake in combinations(dwarfs, 2):
        
        # 3. 전체 합에서 가짜 2명의 키를 뺐을 때 100이 남는다면 정답
        if total_sum - sum(fake) == 100:
            
            # 4. 리스트 컴프리헨션: 가짜 난쟁이가 아닌 진짜 난쟁이들만 추출
            real_dwarfs = [d for d in dwarfs if d not in fake]
            
            # 5. 결과 출력 (줄바꿈으로 합치기)
            print('\n'.join(map(str, real_dwarfs)))
            break

if __name__ == '__main__':
    solve()