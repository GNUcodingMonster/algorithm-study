# 문제: 백준 15650번 N과 M (2)
# 알고리즘: 백트래킹 (Backtracking), DFS
# 풀이 방법: 상태 공간 트리를 탐색하며 오름차순 조건을 만족하는 조합(Combination) 구하기

import sys

# 입력 속도 최적화
input = sys.stdin.readline

N, M = map(int, input().split())

# 탐색 과정에서 선택된 숫자를 담을 리스트 (스택 역할)
result = []

def dfs(start_n):
    # Base Condition: M개의 숫자를 모두 골랐을 때 출력하고 이전 노드로 돌아감
    if len(result) == M:
        # 리스트의 요소들을 공백으로 구분하여 한 번에 출력 (언패킹)
        print(*result)
        return
    
    # start_n부터 N까지 탐색하여 중복을 방지하고 오름차순(조합)을 유지함
    for i in range(start_n, N + 1):
        result.append(i)   # 1. 노드 방문 (숫자 선택)
        dfs(i + 1)         # 2. 다음 깊이로 이동 (현재 선택한 숫자 다음부터 탐색)
        result.pop()       # 3. 탐색을 마치면 되돌아와서 숫자 제거 (백트래킹)

# 1부터 탐색 시작
dfs(1)
