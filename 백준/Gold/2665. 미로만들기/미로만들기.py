import sys , heapq
from collections import deque
N = int(sys.stdin.readline().strip())
matrix = []
for i in range(N):
    mazedata = sys.stdin.readline().strip()
    row = []
    for j in range(len(mazedata)):
        row.append(int(mazedata[j]))
    matrix.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x,y):
    #최소 벽 부순 횟수 기록 배열
    dist =[[float('inf')]*N for _ in range(N)]
    dist[x][y] = 0
    
    pq = [(0,x,y)]
    
    while pq:
        block_count, x, y = heapq.heappop(pq)
        
        #목표지점
        if x == N-1 and y == N-1:
            #최소 블록파괴수를 비교해서 반환해야함
            return block_count 
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0 <= nx <N and 0 <= ny <N:
                # 다음 지점이 벽일 경우 (+1)
                next_count=block_count
                if matrix[nx][ny] ==0:
                    next_count = block_count+1
                
                if next_count<dist[nx][ny]:
                    dist[nx][ny] = next_count
                    heapq.heappush(pq,(next_count,nx,ny))
                    
result = bfs(0,0)
print(result)