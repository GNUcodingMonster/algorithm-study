"""
* 문제: 백준 15649번 (N과 M (1))
* 분류: 백트래킹, 순열
* 풀이: itertools.permutations와 제너레이터 표현식을 활용한 1줄 숏코딩
* 시간 복잡도: O(N! / (N-M)!)

[핵심 로직]
1. 조합(combinations)과 달리 순서가 다르면 다른 경우의 수로 취급하는 순열(permutations) 문제.
2. DFS 백트래킹으로 직접 방문 처리(visited 배열)를 하며 순열을 구하는 대신, 파이썬 내장 라이브러리를 사용하여 코드를 극도로 압축.
3. range(1, N + 1) 객체를 바로 재료로 전달하여 메모리를 절약.
4. map(str)로 숫자를 문자로 바꾸고, ' '.join()과 '\n'.join()을 제너레이터와 엮어 단 1번의 print()로 전체 결과를 출력 (I/O 부하 최소화).
"""

import sys
from itertools import permutations

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    # 제너레이터와 join을 활용하여 순열 생성 및 출력을 단 한 줄로 처리
    print('\n'.join(' '.join(map(str, p)) for p in permutations(range(1, N + 1), M)))

if __name__ == '__main__':
    solve()