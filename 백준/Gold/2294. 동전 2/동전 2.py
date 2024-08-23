import sys

N, K =map(int,sys.stdin.readline().split())

coins = []
dp = [float('inf')] * (K+1)
dp[0] =0
for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))
    

for coin in coins:
    for i in range(coin, K+1):
        dp[i] = min(dp[i],dp[i-coin]+1)
        
if dp[K]==float('inf'):
    print(-1)
else:
    print(dp[K])