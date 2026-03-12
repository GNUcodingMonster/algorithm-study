# 문제: 백준 2579번 계단 오르기
# 알고리즘: 동적 계획법 (Dynamic Programming)
# 풀이 방법: 연속 3계단을 밟지 않는 조건을 만족하는 최적 부분 구조(Optimal Substructure)의 점화식 도출

import sys

# 입력 속도 최적화
input = sys.stdin.readline

N = int(input())

# 계단의 개수가 최대 300개이므로, 인덱스 에러 방지를 위해 크기가 301인 배열 초기화
stairs = [0] * 301
for i in range(1, N + 1):
    stairs[i] = int(input())

# 해당 계단까지 도달했을 때의 최대 점수를 저장할 DP 테이블
dp = [0] * 301

# 초기값 설정 (N이 1, 2, 3일 때의 예외 처리 포함)
dp[1] = stairs[1]
if N >= 2:
    dp[2] = stairs[1] + stairs[2]
if N >= 3:
    # 3번째 계단은 (1번째+3번째) 또는 (2번째+3번째) 중 최댓값
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 점화식을 이용한 바텀업(Bottom-Up) 방식 DP 수행
for i in range(4, N + 1):
    # i번째 계단에 도달하는 두 가지 경우의 수 중 최댓값 선택
    # 1. 두 계단 전(i-2)에서 바로 올라온 경우
    # 2. 세 계단 전(i-3)에서 올라오고, 한 계단 전(i-1)을 거쳐서 올라온 경우 (연속 3계단 방지)
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    
print(dp[N])
