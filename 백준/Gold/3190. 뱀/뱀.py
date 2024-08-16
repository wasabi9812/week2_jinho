import sys
from collections import deque
N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
apples=[]
for i in range(K):
    a,b =map(int,sys.stdin.readline().split())
    apples.append([a-1,b-1])
    
L = int(sys.stdin.readline().strip())

directionDict =dict()
for i in range(L):
    X, C = sys.stdin.readline().split()
    directionDict[int(X)] = C

graph = [[0]*N for _ in range(N)] # 그래프NxN
dx = [0,1,0,-1]
dy = [1,0,-1,0]

graph[0][0]=1 # 뱀위치

for i in range(K): #사과위치
    ax = apples[i][0]
    ay = apples[i][1]
    graph[ax][ay] = 2


direction = 0
cnt = 0
x,y =0,0

queue = deque()
queue.append((0,0))

def turn(alpha):
    global direction
    if alpha =='L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
        
while True:
    cnt+=1
    x +=dx[direction]
    y +=dy[direction]
    
    if x<0 or x>=N or y<0 or y>=N: # 벽에 박았을때
        break
    
    if graph[x][y] ==2: # 다음좌표가 사과일때
        graph[x][y] =1 # 일단 머리가갔으니 그좌표에 1
        queue.append((x,y)) # 뱀이 간거니 스택에 올리고
        if cnt in directionDict:
            turn(directionDict[cnt])
            
    elif graph[x][y] ==0: # 다음좌표가 아무것도 없을때
        graph[x][y] = 1
        queue.append((x,y))
        tx,ty =queue.popleft()
        graph[tx][ty] =0
        if cnt in directionDict:
            turn(directionDict[cnt])
            
    else:
        break
    
print(cnt)