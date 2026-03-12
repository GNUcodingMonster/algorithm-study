# 문제: 백준 2667번 단지번호붙이기
# 알고리즘: 너비 우선 탐색(BFS), 그래프 탐색
# 풀이 방법: 2차원 배열에서 dx, dy를 활용한 상하좌우 탐색 및 연결 요소(Connected Component) 개수 구하기

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

# 띄어쓰기 없이 붙어있는 문자열 입력을 1자리 정수 리스트로 변환
graph = [list(map(int, input().strip())) for _ in range(N)]

# 방문 여부를 체크할 2차원 배열 초기화
visited = [[False] * N for _ in range(N)]

# 상, 하, 좌, 우 네 방향 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 각 단지별 집의 수를 저장할 배열
result = []

def bfs(start_x, start_y):
    count = 1  # 처음 발견한 집도 카운트에 포함
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 상하좌우 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 1. 지도의 범위를 벗어나지 않고
            if (nx >= 0 and nx < N) and (ny >= 0 and ny < N):
                # 2. 집이 존재(1)하며 아직 방문하지 않은 곳이라면
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1 # 집의 개수 누적
                    
    # 탐색이 끝나면 해당 단지에 속한 집의 총 개수 반환
    return count                     
                        
# 지도의 모든 좌표를 완전 탐색하며 새로운 단지의 시작점을 찾음
for x in range(N):
    for y in range(N):
        # 집(1)이 있고 방문하지 않은 좌표에서만 새로운 BFS 탐색 시작
        if graph[x][y] == 1 and not visited[x][y]:
            result.append(bfs(x, y))

# 단지 내 집의 수를 오름차순 정렬 (문제 요구사항)
result.sort()

# 총 단지 수 출력
print(len(result))
# 각 단지별 집의 수 출력
for i in range(len(result)):
    print(result[i])
