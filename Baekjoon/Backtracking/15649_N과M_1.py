# 문제: 백준 15649번 N과 M (1)
# 알고리즘: 백트래킹 (Backtracking), DFS
# 풀이 방법: 상태 공간 트리를 탐색하며 중복 없이 순서가 부여된 순열(Permutation) 구하기

import sys

# 입력 속도 최적화
input = sys.stdin.readline

N, M = map(int, input().split())

# 탐색 과정에서 선택된 숫자를 담을 리스트 (스택 역할)
result = []

def dfs():
    # Base Condition: 원하는 길이(M)에 도달하면 수열을 출력하고 되돌아감
    if len(result) == M:
        print(*result)
        return
    
    # 순열이므로 항상 1부터 N까지 모든 숫자를 탐색의 후보로 둠
    for i in range(1, N + 1):
        # 단, 이미 수열에 포함된 숫자는 중복해서 고를 수 없으므로 제외함 (방문 처리 역할)
        if i not in result:
            result.append(i)   # 1. 숫자 선택
            dfs()              # 2. 다음 깊이로 재귀 호출
            result.pop()       # 3. 되돌아오면 숫자 제거 (백트래킹)

dfs()
