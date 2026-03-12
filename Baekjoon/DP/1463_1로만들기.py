# 문제: 백준 1463번 1로 만들기
# 알고리즘: 동적 계획법 (Dynamic Programming)
# 풀이 방법: 작은 문제부터 해결해 나가는 바텀업(Bottom-Up) 방식의 타뷸레이션 활용

import sys

input = sys.stdin.readline

N = int(input())

# 연산 횟수의 최솟값을 저장할 DP 테이블 초기화
# 인덱스와 숫자를 직관적으로 맞추기 위해 N+1 크기로 생성
dp = [0] * (N + 1)

def DP(n):
    # 2부터 N까지 차례대로 최적의 해를 구해나감 (Bottom-Up)
    for i in range(2, n + 1):
        # 1. 현재 수에서 1을 빼는 경우를 기본 연산 횟수로 설정
        dp[i] = dp[i-1] + 1
        
        # 2. 현재 수가 2로 나누어떨어지는 경우, 
        # (1을 뺀 경우)와 (2로 나눈 경우) 중 더 작은 연산 횟수로 갱신
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        
        # 3. 현재 수가 3으로 나누어떨어지는 경우, 
        # 현재까지의 최솟값과 (3으로 나눈 경우) 중 더 작은 연산 횟수로 갱신
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

DP(N)
print(dp[N])
