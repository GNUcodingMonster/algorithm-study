# 문제: 백준 2309번 일곱 난쟁이
# 메모리: 약 31120 KB, 시간: 약 40 ms
# 풀이 방법: 완전 탐색 (DFS / 백트래킹을 활용한 조합 구현)

import sys

# 입력 속도 향상을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 9명의 난쟁이 키를 입력받아 리스트로 저장
arr = [int(input()) for _ in range(9)]

# 결과를 오름차순으로 출력해야 하므로 미리 정렬
arr.sort()

# 선택된 난쟁이들을 담을 리스트 (스택 역할)
visited = []

def dfs(start_node):
    # Base Condition: 7명의 난쟁이를 모두 골랐을 때
    if len(visited) == 7:
        # 고른 7명의 키의 합이 100이라면 정답
        if sum(visited) == 100:
            for j in visited:
                print(j)
            # 정답이 여러 개일 수 있으나 하나만 출력하면 되므로 프로그램 즉시 종료
            exit() 
        return
    
    # start_node부터 8번 인덱스(총 9명)까지 탐색
    for i in range(start_node, 9):
        # 1. 현재 난쟁이를 선택
        visited.append(arr[i])
        
        # 2. 다음 난쟁이를 고르기 위해 재귀 호출 (현재 인덱스 + 1)
        dfs(i + 1)
        
        # 3. 재귀가 끝나고 돌아오면, 다른 조합을 찾기 위해 현재 난쟁이를 다시 뺌 (백트래킹)
        visited.pop()

# 0번 인덱스부터 탐색 시작
dfs(0)
