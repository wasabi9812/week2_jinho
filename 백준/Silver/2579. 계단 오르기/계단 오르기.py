import sys

N = int(sys.stdin.readline().strip())
data = []
data.append(0)
for i in range(N):
    data.append(int(sys.stdin.readline()))

# 6
# 10
# 20
# 15
# 25
# 10
# 20

# print(data)

dp = [0 for _ in range(N+1)]
if N >= 1:
    dp[1] = data[1]
if N >= 2:
    dp[2] = dp[1] + data[2]
if N>=3:
    for i in range(3,N+1):# 내 계단 위치   
          dp[i] = max(dp[i-3]+data[i-1],dp[i-2])+data[i]
      
print(dp[N])