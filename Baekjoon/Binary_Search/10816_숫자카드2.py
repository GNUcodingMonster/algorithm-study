# 문제: 백준 10816번 숫자 카드 2
# 알고리즘: 이분 탐색 (Binary Search), 정렬
# 풀이 방법: bisect 라이브러리를 활용하여 upper_bound와 lower_bound의 차이로 개수 탐색

import sys
from bisect import bisect_left, bisect_right

# 입력 데이터가 최대 500,000개이므로 sys.stdin.readline 필수 사용
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
card_find = list(map(int, input().split()))

# 이분 탐색을 위한 사전 오름차순 정렬
card.sort()

# 찾고자 하는 각 카드에 대해 (우측 경계 인덱스 - 좌측 경계 인덱스)를 계산하여 개수 파악
for i in card_find:
    count = bisect_right(card, i) - bisect_left(card, i)
    print(count, end=' ')
