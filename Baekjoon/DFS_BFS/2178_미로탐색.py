# 문제: 백준 2178번 미로 탐색
# 알고리즘: 너비 우선 탐색(BFS), 그래프 탐색
# 풀이 방법: BFS의 레벨(Depth) 탐색 특성을 활용하여 2차원 미로의 최단 거리 도출

import sys
from collections import deque

# 입력 속도 최적화
input = sys.stdin.readline

N, M = map(int, input().split())

# 띄어쓰기 없이 입력되는 미로 데이터를 1자리 정수 2차원 배열로 파싱
graph = [list(map(int, input().strip())) for _ in range(N)]

# 상하좌우 탐색을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 1. 미로 공간을 벗어나지 않고, 2. 이동할 수 있는 칸(1)인 경우
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                
                # 핵심: 이전 칸의 거리 값에 +1을 하여 현재 칸에 최단 거리 기록 (방문 처리 겸용)
                graph[nx][ny] = graph[x][y] + 1
                
                # 목적지(N-1, M-1)에 도달하면 즉시 기록된 거리를 반환하고 탐색 종료
                if nx == N - 1 and ny == M - 1: 
                    return graph[nx][ny]

# 시작점 (0, 0)부터 탐색 시작
print(bfs(0, 0))
