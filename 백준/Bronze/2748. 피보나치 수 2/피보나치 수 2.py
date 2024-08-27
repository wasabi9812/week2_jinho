import sys
N = int(sys.stdin.readline().strip())

# 인덱스 에러를 방지하기 위해 N이 1 또는 2일 때의 예외처리
if N == 1:
    print(1)
elif N == 2:
    print(1)
else:
    dp = [0 for _ in range(N+1)]

    dp[1] = 1
    dp[2] = 1

    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[N])