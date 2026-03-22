import sys

input = sys.stdin.readline

def binary_search_parametric(N, M, trees):
    #이분탐색으로 최댓값 구함
    left = 0
    right = max(trees)
    best_answer = -1

    while left <= right:
        mid = (left+right)//2
        if check_condition(trees,mid)>=M: #잘린 나무길이가 M보다 길면
            best_answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return best_answer

def check_condition(trees,n):
    return sum(tree - n for tree in trees if tree -n > 0) 

def solution():
    #나무 수, 나무 길이, 나무 리스트 입력받고
    N, M = map(int, input().split())
    #나무 리스트 정렬
    trees = list(map(int,input().split()))
    #최댓값 출력
    print(binary_search_parametric(N,M,trees))
    return

solution()

