import sys

# 입력 받기
N = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())

data2 = []
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    data2.append([a-1, b-1])  # 인덱스를 0부터 사용하기 위해 -1

# DP 테이블 초기화
dp = [[0 for _ in range(N)] for _ in range(N)]

# 길이 1인 경우 (자기 자신만 있는 부분 수열)
for i in range(N):
    dp[i][i] = 1

# 길이 2인 경우
for i in range(N-1):
    if data[i] == data[i+1]:
        dp[i][i+1] = 1

# 길이 3 이상인 경우
for length in range(3, N+1):  # length는 부분 수열의 길이
    for i in range(N-length+1):
        j = i + length - 1  # 끝 인덱스 계산
        if data[i] == data[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

# 질의에 대한 응답
for a, b in data2:
    print(dp[a][b])   