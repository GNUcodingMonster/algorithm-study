"""
* 문제: 백준 15650번 (N과 M (2))
* 분류: 백트래킹, 조합론
* 풀이: itertools.combinations와 제너레이터 표현식을 활용한 1줄 숏코딩
* 시간 복잡도: O(N C M)

[핵심 로직]
1. 백트래킹(DFS)으로 직접 상태 공간 트리를 탐색하는 대신, 파이썬 내장 라이브러리인 combinations를 사용하여 오름차순 조합을 즉시 생성.
2. 불필요한 리스트 메모리 할당을 막기 위해 range() 객체를 조합의 재료로 직접 전달.
3. 생성된 숫자 튜플을 map(str)을 통해 문자열로 일괄 변환.
4. 안쪽의 ' '.join()으로 숫자 사이를 띄우고, 바깥쪽의 '\n'.join()과 제너레이터 표현식(Generator Expression)을 결합하여 단 1번의 print() 호출로 전체 정답을 출력(I/O 최적화).
"""

import sys
from itertools import combinations

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    # 제너레이터와 join을 활용한 궁극의 1줄 출력
    print('\n'.join(' '.join(map(str, comb)) for comb in combinations(range(1, N + 1), M)))

if __name__ == '__main__':
    solve()