import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

def binary_search(A,b):
    start = 0
    end = len(A)-1

    while start<=end:
        mid = (start + end)//2
        if A[mid] == b:
            return 1
        elif A[mid] < b:
            start = mid+1
        else:
            end = mid-1
    return 0


for b in B:
    if binary_search(A,b):
        print(1)
    else:
        print(0)