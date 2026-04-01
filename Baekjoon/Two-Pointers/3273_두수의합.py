import sys

input = sys.stdin.readline

def two_pointers(n,sorted_a,target_sum):
    start = 0
    end = n - 1
    count = 0

    while(start < end):
        current_sum = sorted_a[start]+sorted_a[end]
        if current_sum < target_sum:
            start += 1
        elif current_sum > target_sum:
            end -= 1
        else:
            count += 1
            start += 1
            end -= 1

    return count

def solution(n,a,target_sum): #solution 함수는 반드시 결과값을 리턴함
    return two_pointers(n,sorted(a),target_sum) #배열 정렬해서 전달

def main(): #입력 받고, 최종 결과 출력
    n = int(input())
    a = list(map(int,input().split()))
    target_sum = int(input())
    solution(n,a,target_sum)

if __name__ == "__main__":
    main()
            