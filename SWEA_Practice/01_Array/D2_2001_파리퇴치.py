import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    def swing(x,y,M):
        total = 0
        for i in range(M):
            for j in range(M):
                    total += graph[x+i][y+j]
        return total
    
    result = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            temp = swing(x,y,M)
            if temp > result: result = temp

    print(f"#{test_case} {result}")
                
    