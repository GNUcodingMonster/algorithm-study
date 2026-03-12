# 문제: 백준 1715번 카드 정렬하기
# 알고리즘: 그리디 (Greedy), 자료 구조, 우선순위 큐 (Priority Queue)
# 풀이 방법: 매 턴마다 가장 작은 두 카드 묶음을 꺼내어 합치고, 그 합을 다시 힙에 넣는 과정을 반복

import sys
import heapq

# 입력 속도 최적화
input = sys.stdin.readline

N = int(input())
C = [int(input()) for _ in range(N)]

# 최소 힙으로 사용할 리스트
hq = []
num = 0

# 입력받은 카드 묶음의 크기를 모두 힙에 삽입
for c in C:
    heapq.heappush(hq, c)

# 힙에 카드 묶음이 1개만 남을 때까지 반복 (N이 1인 경우 while문이 실행되지 않아 0 출력)
while len(hq) > 1:
    # 가장 크기가 작은 두 카드 묶음을 꺼냄
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    
    # 두 묶음을 합치기 위한 비교 횟수를 누적
    num += a + b
    
    # 합쳐진 새로운 카드 묶음을 다시 힙에 삽입
    heapq.heappush(hq, a + b)

print(num)
