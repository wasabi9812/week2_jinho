import sys

N = int(sys.stdin.readline().strip())
data = []
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
    
dp = [[0 for _ in range(N)] for _ in range(N)]
# dp테이블 초기화
    
for length in range(2,N+1): # 1개 행렬은 연산횟수 0으로 2부터 시작 N까지
    for i in range(N-length+1):
        j = i+length-1
        dp[i][j] =sys.maxsize
        for k in range(i,j):
            #Cost같은 임시변수로 갱신하고 min으로 비교하지않으면 초기값과 비교해 0으로 변함
            cost = dp[i][k]+dp[k+1][j]+data[i][0]*data[k][1]*data[j][1]
            dp[i][j] = min(dp[i][j],cost)

print(dp[0][N-1])