import sys
# 이분그래프 dfs구현
sys.setrecursionlimit((10**7))

def dfs(n, g):
    visited[n] = g
    
    for i in graph[n]:
        if not visited[i]:
            a = dfs(i, -g)
            if not a:
                return False
        elif visited[i] ==visited[n]:
            return False
    return True


N = int(sys.stdin.readline()) #시행횟수
for k in range(N):
    V,E = map(int,sys.stdin.readline().split())
    
    visited = [0]*(V+1)
    
    graph =[[] for i in range(V+1)]
    for i in range(E):
        a, b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if not visited[i]:
            result = dfs(i,1)
            if not result:
                break
            
    if result: 
        print("YES")
    else:
        print("NO")
