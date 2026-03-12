# 문제: 백준 7576번 토마토
# 알고리즘: 너비 우선 탐색(BFS), 그래프 탐색
# 풀이 방법: 익은 토마토가 여러 개일 수 있으므로, 모든 시작점을 큐에 미리 넣고 동시다발적으로 퍼져나가는 다중 시작점 BFS 구현

import sys
from collections import deque

# 입력 속도 최적화
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

# 1. 맵 전체를 탐색하며 익은 토마토(1)의 위치를 모두 큐에 삽입 (다중 시작점 세팅)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
            
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 2. 범위 내에 있고, 익지 않은 토마토(0)가 있다면
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                queue.append((nx, ny))
                # 3. 이전 토마토의 값 + 1을 하여 며칠이 걸렸는지 누적 기록 (방문 처리 겸용)
                graph[nx][ny] = graph[x][y] + 1

# BFS 실행 (큐에 미리 넣어둔 모든 1에서부터 동시다발적으로 시작됨)
bfs()

result = 0

# 4. 탐색 종료 후 결과 판별
for row in graph:
    # 맵에 익지 않은 토마토(0)가 하나라도 남아있다면 모두 익지 못하는 상황이므로 -1 출력 후 종료
    if 0 in row:
        print(-1)
        exit(0)
    # 가장 오래 걸린 일수(최댓값)를 갱신
    result = max(result, max(row))

# 처음 익은 토마토가 1부터 시작했으므로, 실제 걸린 일수는 -1을 해주어야 함
print(result - 1)
