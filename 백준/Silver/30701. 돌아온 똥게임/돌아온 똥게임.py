import sys
import heapq

# 첫 번째 줄에서 N, D를 받음
N, D = map(int, sys.stdin.readline().split())

# 몬스터와 장비를 저장할 리스트
monsters = []
weapons = []

# N개의 방 정보를 처리
for _ in range(N):
    A, X = map(int, sys.stdin.readline().split())
    if A == 1:
        heapq.heappush(monsters, X)  # 몬스터는 오름차순으로 처리
    else:
        heapq.heappush(weapons, X)  # 장비는 작은 것부터 사용해야 함

clearcnt = 0

# 몬스터와 장비를 처리
while monsters:
    monster = heapq.heappop(monsters)  # 최소값(가장 작은 몬스터)을 pop

    if monster < D:  # 현재 전투력으로 몬스터를 처리할 수 있으면
        D += monster  # 그 몬스터를 잡고 전투력을 증가
        clearcnt += 1
    else:
        if weapons:  # 장비가 남아 있으면
            heapq.heappush(monsters, monster)  # 몬스터를 다시 힙에 넣고
            D *= heapq.heappop(weapons)  # 장비를 사용하여 전투력 증가
            clearcnt += 1
        else:
            break  # 장비도 없고 몬스터도 처리할 수 없으면 중단

# 결과 출력
print(clearcnt + len(weapons))