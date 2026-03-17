"""
* 문제: 백준 10816번 (숫자 카드 2)
* 분류: 자료 구조, 이분 탐색, 해시 맵
* 풀이: collections.Counter를 활용한 해시 맵 탐색
* 시간 복잡도: O(N + M) (이분 탐색 O(N log N + M log N)보다 압도적으로 빠름)

[핵심 로직]
1. 탐색 속도를 높이기 위해 배열 정렬이나 bisect 대신 해시 맵(Dictionary) 구조 사용.
2. collections.Counter를 이용해 카드의 개수를 O(N)만에 매핑.
3. 타겟 카드를 조회할 때 딕셔너리의 .get() 메서드를 사용하여 O(1)의 속도로 개수 반환.
4. map과 join을 활용하여 출력 속도 및 메모리 사용량 최적화.
"""

import sys
from collections import Counter

def solve():
    input = sys.stdin.readline
    
    # 1. 상근이가 가진 카드 입력 (문자열 리스트 그대로 유지)
    N = int(input())
    cards = input().split()
    
    # 2. Counter를 이용해 카드별 개수를 해시 맵으로 생성 -> O(N)
    card_count = Counter(cards)
    
    # 3. 찾아야 할 타겟 카드 입력
    M = int(input())
    targets = input().split()
    
    # 4. 해시 맵에서 타겟 카드의 개수를 O(1)로 조회
    # target이 card_count에 없으면 기본값 0을 반환하도록 설정
    answer = [str(card_count.get(target, 0)) for target in targets]
    
    # 5. 리스트 요소들을 공백으로 이어붙여 한 번에 출력 (I/O 최적화)
    print(' '.join(answer))

if __name__ == '__main__':
    solve()