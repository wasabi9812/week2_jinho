import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    coins = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline().strip())
    
    dp = [0 for _ in range(M+1)]
    dp[0]=1
    for coin in coins:
        for i in range(coin,M+1):
            dp[i]+=dp[i-coin]
            
    print(dp[M])