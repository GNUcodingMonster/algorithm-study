# 문제: 백준 10026번 적록색약
# 알고리즘: 너비 우선 탐색(BFS), 그래프 탐색
# 풀이 방법: 원본 배열에서 1차 탐색 후, 'R'을 'G'로 치환하고 방문 배열을 초기화하여 2차 탐색을 진행하는 함수 재활용 기법

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

# 띄어쓰기 없는 문자열 입력을 2차원 리스트로 변환
graph = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 1. 범위 내에 있고, 2. 미방문 상태이며, 3. 현재 색상과 다음 색상이 같은 경우만 탐색
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                queue.append((nx, ny))
                visited[nx][ny] = True

# 1. 적록색약이 아닌 사람이 봤을 때의 구역 개수 구하기
count_normal = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            count_normal += 1

# 2. 적록색약인 사람을 위한 맵 상태 변환 ('R'을 모두 'G'로 통일)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

# 두 번째 탐색을 위해 visited 배열 초기화
visited = [[False] * N for _ in range(N)]
count_impaired = 0
            
# 3. 적록색약인 사람이 봤을 때의 구역 개수 구하기
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            count_impaired += 1
            
print(count_normal, count_impaired)
