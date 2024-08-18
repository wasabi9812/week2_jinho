import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
# 인접리스트


network = [[]*(N+1) for _ in range(N+1)]

for i in range(K):
    a, b = map(int,sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)

visited =[0]*(N+1)

cnt=0
def DFS(virus):
    global cnt
    visited[virus]=1

    for i in network[virus]:
        if (visited[i]==0):
            DFS(i)
            cnt+=1

DFS(1)
print(cnt)