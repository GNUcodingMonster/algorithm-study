import random

def match(index_list): # [3] v
    #셔플된 index 배열을 두개씩 pop한뒤 e1, e2 반환
    if len(index_list)>=2:
        e1, e2 = index_list.pop(), index_list.pop()
    elif len(index_list)== 1:
        e1, e2 = index_list.pop(), -1 #하나만 남은 경우 e2를 -1로 전달
    return e1, e2

def play_game(e1, e2 , G, populations, e_list, scores): # [4] v
    #match된 객체 두개의 게임을 G번 진행하고 각 라운드 액션에 따라 get_scores(a1, a2)(scores를 기준으로 점수를 부여)하고 e_list를 업데이트함
    #부전승인지 확인
    if e2 == -1:
        return e_list
    specie_e1, ri_e1 = get_species(e1,populations)
    specie_e2, ri_e2 = get_species(e2,populations)
    e1_last_move, e2_last_move = 'D','D' #R은 첫무브가 무조건 배신이므로 D로 초기화
    for i in range(G):
        a1, a2 = action_by_entity(specie_e1,e2_last_move), action_by_entity(specie_e2,e1_last_move)
        score_e1, score_e2 = get_scores(a1,a2,scores)
        e_list[specie_e1][ri_e1]+= score_e1
        e_list[specie_e2][ri_e2]+= score_e2
        e1_last_move = a1
        e2_last_move = a2
    return e_list

def get_scores(a1, a2, scores): # [3] v
    m, n, k, l = scores
    if a1 == 'C':
        if a2 == 'C':
            return m , m
        else:
            return k, l
    else:
        if a2 == 'C':
            return l, k
        else:
            return n, n

def action_by_entity(species,op_last_move): # [2] v
    #개체별로 행동을 설정하고 특히 R개체는 상대 마지막 움직임에 따라 행동을 달리한다.
    #액션(C/D)을 리턴한다
    if species == 0:
        return 'C'
    if species == 1:
        return 'D'
    if species == 2:
        return op_last_move


def get_species(e,populations): # [1] v
    #개체 인덱스와 개체 분포를 비교하여 개체 종류를 S,B,R중 에서 한개 그리고 종족 내에서의 인덱스(로컬 인덱스)도 리턴한다.
    S,B,R = populations
    if e < S:
        species, local_index = 0 , e # S이면 0
    elif e< S+B:
        species, local_index = 1 , e-S #B이면 1
    else:
        species, local_index = 2 , e-(S+B) #R이면 2
    return species, local_index

def update_populations(e_list,Rep): #[5]
    #Rep에 따라 개체를 생성 소멸하고 e_list에 업데이트한다.
    #populations도 업데이트한다.
    new_e_list = [[],[],[]]
    new_populations = []
    for specie in range(len(e_list)): #종족별
        for local_idx in range(len(e_list[specie])): #rocal index
            if e_list[specie][local_idx]<= 0:
                continue
            if e_list[specie][local_idx] < Rep:
                new_e_list[specie].append(e_list[specie][local_idx])
            else:
                new_e_list[specie].append(e_list[specie][local_idx]//2)
                new_e_list[specie].append(e_list[specie][local_idx]//2)
        new_populations.append(len(new_e_list[specie]))
        
    return new_e_list, new_populations
    
                



def solutions(scores,populations,rules): # [6]
    E, Rep, G, T=rules
    # 초기 e_list 초기화
    e_list = [[E]*count for count in populations]

    for _ in range(T):
        # index_list 초기화
        index_list = list(range(sum(populations)))
        # 매 라운드 시작 시 index_list 셔플
        random.shuffle(index_list)
        while (len(index_list)):
            e1, e2 = match(index_list)
            e_list=play_game(e1, e2 , G, populations, e_list, scores)
        e_list, populations = update_populations(e_list,Rep)

    return populations

# 실행 예시 (맨 아래에 추가)
if __name__ == "__main__":
    scores = [3, 1, 0, 5]
    populations = [10, 10, 10]
    rules = [10, 100, 5, 100]
    result = solutions(scores, populations, rules)
    print("최종 살아남은 생태계:", result)