# 문제: 백준 14503번 로봇 청소기
# 알고리즘: 시뮬레이션 (Simulation), 구현 (Implementation)
# 풀이 방법: 문제에서 제시한 로봇의 작동 룰 3가지를 조건문과 방향 벡터를 활용해 그대로 코드로 구현

import sys

# 입력 속도 최적화
input = sys.stdin.readline

N, M = map(int, input().split())

# 로봇 청소기의 현재 좌표(r, c)와 바라보는 방향(d)
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 북(0), 동(1), 남(2), 서(3) 방향 벡터 (문제 조건과 일치하도록 인덱스 설정)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소하는 칸의 개수
move = 0

# 시뮬레이션 시작
while True:
    # 1. 현재 위치를 청소한다. (청소한 빈 칸은 2로 마킹하여 벽(1)과 구분)
    if graph[r][c] == 0:
        graph[r][c] = 2
        move += 1
    
    # 네 방향 중 청소할 빈 칸이 있는지 확인하는 플래그
    blank = False

    # 2. 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
    for _ in range(4):
        # 반시계 방향으로 90도 회전 (0->3, 3->2, 2->1, 1->0)
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        
        # 지도를 벗어나지 않고, 청소하지 않은 빈 칸(0)이 존재한다면
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            r = nx
            c = ny
            blank = True
            break # 한 칸 전진했으므로 탐색 중지하고 다시 1번부터 진행
    
    # 3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우
    if not blank:
        # 바라보는 방향을 유지한 채로 한 칸 후진
        back_x = r - dx[d]
        back_y = c - dy[d]
        
        # 후진할 수 있는 곳이 지도를 벗어나지 않고 벽(1)이 아니라면 후진 (청소한 곳(2)이어도 후진 가능)
        if 0 <= back_x < N and 0 <= back_y < M and graph[back_x][back_y] != 1:
            r, c = back_x, back_y
        # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
        else:
            break

print(move)
