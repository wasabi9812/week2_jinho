import sys

N = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))

dp = [1] * N  # 모든 원소를 1로 초기화 (자기 자신만 포함하는 수열의 길이)

# LIS 계산
for i in range(N):
    for j in range(i+1, N):
        if data[i] < data[j]:
            dp[j] = max(dp[j], dp[i] + 1)  # max자체가 배열전체를 비교해줄수있음

# 결과 출력
result = max(dp)
print(result)
