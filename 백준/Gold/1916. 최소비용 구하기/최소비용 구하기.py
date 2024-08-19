import sys ,heapq
INF = int(1e9)
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = [[] for i in range(N+1)]
distance = [INF]*(N+1)  # 거리배열 생성하면서 아주큰값 생성

for i in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    
S, E = map(int,sys.stdin.readline().split())


def dijkstra(S):
    queue = []
    distance[S] = 0
    heapq.heappush(queue,(0,S))
    
    while queue:
        curCost, curNode,  = heapq.heappop(queue)
        if distance[curNode]<curCost:
            if curNode == E:
                break
            else:
                continue
        for i in graph[curNode]:
            cost = curCost+i[1]
            if distance[i[0]]>cost:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost, i[0]))

dijkstra(S)
print(distance[E])
# print(graph)
                
                