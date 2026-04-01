import sys

input = sys.stdin.readline

def two_pointers(N,M,A):
    #배열 받고, 배열 길이 받아서 start, end 설정하고 total 구해서
    end = 0
    total = 0
    count = 0
    for start in range(N):
        #total과 M 조건문 따라 count값 증가 
        while total < M and end < N :
            total += A[end]
            end += 1
        if total == M:
            count += 1
        total -= A[start]


    return count
            


def solution():
    #자료 입력받아서 N,M, A[]에 저장
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    #two_pointers 값 출력
    print(two_pointers(N,M,A))

solution()
