import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())

graph = [[] for i in range(N+1)]
indegree = [0]*(N+1) #진입차수
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b]+=1
    
    
queue = deque()
result = []
for i in range(1, N+1):
    if indegree[i]==0:
        queue.append(i)

while queue:
    now = queue.popleft()
    result.append(now)
    for g in graph[now]:
        indegree[g]-=1
        if indegree[g]==0:
            queue.append(g)
            
for res in result:
    print(res)