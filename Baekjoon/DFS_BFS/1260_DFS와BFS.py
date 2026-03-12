# 문제: 백준 1260번 DFS와 BFS
# 알고리즘: 깊이 우선 탐색(DFS), 너비 우선 탐색(BFS), 그래프 이론
# 풀이 방법: 인접 리스트(Adjacency List)를 활용하여 그래프를 구현하고 정렬한 뒤 탐색 진행

import sys
from collections import deque

# 입력 속도 최적화
input = sys.stdin.readline

N, M, V = map(int, input().split())

# 1번부터 N번까지의 정점을 직관적으로 사용하기 위해 N+1 크기의 인접 리스트 생성
graph = [[] for _ in range(N + 1)]

# 양방향(무방향) 간선 연결
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 문제 조건: "방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문"
for i in range(1, N + 1):
    graph[i].sort()

# DFS와 BFS 각각의 방문 처리를 위한 불리언 배열
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

# DFS (깊이 우선 탐색) - 재귀 함수 활용
def dfs(start_node):
    visited_dfs[start_node] = True
    print(start_node, end=' ')
    
    # 현재 정점과 연결된 인접 정점들을 깊이 파고들며 탐색
    for i in graph[start_node]:
        if not visited_dfs[i]:
            dfs(i)

# BFS (너비 우선 탐색) - 큐(Queue) 활용
def bfs(start_node):
    queue = deque([start_node])
    visited_bfs[start_node] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        # 현재 정점과 연결된 인접 정점들을 모두 큐에 넣고 넓게 탐색
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(V)
print() # DFS 출력 후 줄바꿈
bfs(V)
