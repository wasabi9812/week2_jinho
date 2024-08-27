import sys

N, T = map(int,sys.stdin.readline().split())

data = []

for i in range(N):
        data.append(list(map(int,sys.stdin.readline().split())))

dp = [[0 for _ in range(T+1)] for _ in range(N+1)]

for i in range(1,N+1):
    time, score = data[i-1]
    for j in range(1,T+1):
        if time>j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time]+score)
            
print(dp[N][T])
            