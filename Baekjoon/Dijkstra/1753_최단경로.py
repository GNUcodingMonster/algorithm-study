import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

def dijkstra(graph, start, V) : #bfs처럼 하되 heapq에 적제시켜서 최단거리부터 탐색
    #시작점에서 자신의 거리는 0
    distance = [INF] * (V+1)
    distance[start] = 0
    #힙큐 생성해서 코스트 순으로 팝하기 위해 (cost, 노드) 튜플로 넣는다
    pq = []
    heapq.heappush(pq, (0, start))

    #힙큐가 비어있지 않을동안 반복:
    while pq: 
    #현재 힙큐를 팝해서 지금 현재 노드와 현재 비용을 초기화한다.
        current_cost, current_node = heapq.heappop(pq)
    #만약 현재 비용이 distance에 기록된 최저 비용으로 예상된 값보다
        if current_cost > distance[current_node]:
            continue 
    #크다면 이 길은 쓸필요가 없으므로 다음 큐로 넘어간다.
    #작다면 현재 노드와 인접한 노드들을
        for next_node, weight in graph[current_node] :
            cost = current_cost+weight
    #만약 다음큐노드의 디스턴스가 현재 비용에 다음큐 cost를 더한 값보다 크다면
            if distance[next_node]>cost:
                distance[next_node]=cost
                heapq.heappush(pq,(distance[next_node],next_node))
    #다음큐의 디스턴스를 현재 비용 + cost로 업데이트하고
    #큐에 (다음 노드, 비용)을 힙푸쉬한다.
    return distance

def solution():
    V,E = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v,w))
    distance = dijkstra(graph, start, V)
    for i in range(1,V+1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])
    return

solution()
