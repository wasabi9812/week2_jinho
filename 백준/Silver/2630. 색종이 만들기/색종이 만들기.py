import sys

N = int(sys.stdin.readline())
color_matrix = [ [] for _ in range(N)]
for i in range(N):
    color_matrix[i] = list(map(int,sys.stdin.readline().strip().split()))

# print(color_matrix)

white=0
black=0

def dfs(n,x,y): # 다음 쪼갠부분에도 시작포지션 그래서 x,y 매개변수
    global black
    global white
    half = n//2
    if n==1:
        if color_matrix[x][y] ==0:
            white += 1
        else:
            black += 1
        return
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color_matrix[i][j] != color_matrix[x][y]:
                dfs(half, x, y) # 1사분면
                dfs(half, x+half, y) # 2사분면
                dfs(half, x, y+half) # 3사분면
                dfs(half, x+half, y+half) # 4사분면
                return ## 리턴을 안함 !!!!!!!!!
            
    if color_matrix[x][y] ==0:
        white += 1
    else:
        black += 1

dfs(N,0,0)

print(white)
print(black)