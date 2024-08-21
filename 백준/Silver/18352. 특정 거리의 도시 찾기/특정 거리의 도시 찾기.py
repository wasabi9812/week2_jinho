import sys
from collections import deque
N,M,K,X = map(int,sys.stdin.readline().split())
INF = int(1e9)
graph = [[] for i in range(N+1)]

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    

distance =[-1]*(N+1)
queue = deque([X])
distance[X] = 0


while queue:
    m = queue.popleft()
    for i in graph[m]:
        if distance[i] == -1:
            distance[i] = distance[m]+1
            queue.append(i)


if K in distance:
    for i in range(len(distance)):
        if distance[i]==K:
            print(i)
else:
    print(-1)