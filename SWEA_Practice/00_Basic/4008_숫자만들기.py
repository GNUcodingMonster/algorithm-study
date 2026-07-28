# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 초기값 설정
    N = int(input())
    op_count = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    
    #수식을 완성할 때 각 연산자 카드를 모두 사용해야 한다..
    #일단 op_count를 만들어 놨으니 이걸 인덱스 연산자로 참조하면서
    #사칙연산 기호 하나씩 할당하는게 좋을듯한데
    #일단 시간 복잡도를 계산하자면
    #N -1 만큼 for문 돌렸을때
    # op_count[i] 같은 형태로 접근하려고 했는데 이러면 연산자 자리를 바꿔가면서
    # 모든 값을 생성하는데 어려움이 있을거같다. 
    # 일단 만약 N=2라고 생각하면
    # op_count= [1,0,0,0] 이면
    # for n in num :
    #   for i in range(4):
        #   result = result ... 최종 결과는 뭘로 만들어야할까
    # 각 op_counts_temp를 만들어서 저장해놓고 카드를 쓸때마다 뺀다.
    # 재귀를 돌려서 깊이가 N일때 탈출한다면?
    # 일단 결국 계산 형태를 어떻게 할 것인가. result = op(op_idx, result, n) 으로 생각하면 되겠다. 
    # 그럼이제 재귀 함수 구조를 생각해보자.
    # 일단 depth 를 구해서 depth가 5면 탈출한다.
    # depth 5가 아니면
    # result = op(op_idx, result, n)
    # 아 이거 dfs로 해야한다.
    # 결국 다 돌고 돌아왔을때 안했던거 실행해보는게 필요하기 때문이다.
    # dfs 템플릿 다시 보고오자.
    # 보고왔는데 여기는 depth 처리가 없다. current 처럼 단순하게 방문하는것도 아니고... 변형이 필요하다.
    '''
    def dfs_template(current, graph, visited):
    # 1. 현재 노드 방문 처리
    visited[current] = True
    print(f"현재 방문한 노드: {current}") # 핵심 로직 수행 위치
    
    # 2. 인접 노드 탐색
    for next_node in graph[current]:
        # 아직 방문하지 않은 노드가 있다면, 즉시 그곳으로 깊게 파고들기(재귀 호출)
        if not visited[next_node]:
            dfs_template(next_node, graph, visited)
    
    '''
    # 어떻게 변형할 것인가? 일단 visited처리를 어떤 방식으로 해야할지 보자.
    # for i in range(4)로 돌릴거다
    # op_count[i] 탐색해서 만약 0이 아니면 값을 -1하고 dfs_template(next_node, graph, visited)..?
    # dfs에 얽메이지 말자.
    # 만약 0이면 
    # recursive_make_num(,depth) 
    # 그냥 op_count말고 풀어서 그냥 N만큼 배열로 만들고 거기에 연산자 넣어 놓을까 했는데
    # 그건 한눈에 보기가 복잡하니까 구조는 지금구조가 더 좋을거같다.
    result = []
    def recursive_make_num(current_num,depth):
        #뭘해야하냐: result를 결국 반환할거다.
        #그런데 인자는 current 값을 넘겨주면 된다.
        #op_count나 numbers 는 외부에 선언해서 참조하자.
        #여기에 필요한건 먼저 depth에 따라 탈출하는 것이다.
        if depth == N:
            #result 밖에다 만들어야겠다.
            result.append(current_num)
            # depth -= 1 를 여기서 하는건 의미가 없다.
            # 지역 변수 이기 때문에
            return
        
        #자 이제 depth가 도달하지 않았을때 즉 계속 깊어지는 구간에서 어떻게 재귀를 호출할 것인가.
        #초기 값 current에 초기로 뭐가 들어올까?
        #여기서 새로운 사실: depth는 결국 현재 연산자를 선택해야할 피연산자의 idx값이다.
        #즉 result = op(op_idx, result, n)에서
        #           op(op_idx, result, numbers(depth)) 처럼 넘기면 된다.
        #그리고 생각해보니까 사칙연산 개수만큼 for 문 돌려야겠다.
        # 그런데 재귀에서는 초기화 구문을 작성하면 계속 돌릴때마다 초기화 되서 안되겠네
        # 초기화는 처음부를때 주는 값으로 하는걸로 한다.
        for i in range(4):
            #만약 사칙연산 개수 남아있으면 사용한다.
            if op_count[i] >0 :
                depth += 1
                op_count[i] -= 1
                recursive_make_num(op(i, current_num, numbers(depth)),depth)
                depth -= 1
                op_count[i] += 1
                #자 그래서 돌아왔다. + 다쓰고 - 있는 상태로 어펜드하고 depth 1빠진 상태로 돌아왔는데
                #여기서 그럼 뭘 해야하냐
                # current_num 쓰면 되니깐 값 돌릴 필요도 없다.
                # 그냥 간다고 생각하면?
                # 디버깅 해보자
                # 그러면 + - * / 순이었다고 생각해보자 각각 하나씩
                # 1,1,1,1에서 0,0,0,0 되고 마지막 depth 5에서 depth 4되서 돌아오고
                # 4번째 중첩에서 빠져나갈거다.
                # depth를 여기서 
            # 자 그럼 생각해보자
            # i = 0 이면 + 개수가 남아있는 만큼 + 될거다. 이후에 - 있는 만큼 - 되고
            # 그러다가 depth가 다 달으면 result에 어펜드하고 그 전으로 돌아오는데
            # 돌아왔을때 연산도 결정해야겠다.
        
    
    # op_count idx 값과 피연산자 두개 전달.
    def op(op_idx, n1, n2):
        if op_idx == 0:
            return n1 + n2
        elif op_idx == 1:
            return n1 - n2
        elif op_idx == 2:
            return n1 * n2
        else:
            return n1 / n2
            
    
    
    
    #저장된 temp min max 불러와서 차 구하고 result에 넣는다
    answer = max(result) - min(result)
    #result값 출력
    print(f'#{test_case} {answer}')

    
    # ///////////////////////////////////////////////////////////////////////////////////
