import sys

S = sys.stdin.readline().strip()

N = int(sys.stdin.readline().strip())

dp = [0]*(len(S)+1)
dp[0] =1
data = []
for i in range(N):
    data.append(sys.stdin.readline().strip())
    
# abc
# abc

for i in range(1,len(S)+1):
    for word in data:
        word_len = len(word) #처음 8나옴 즉 i 8때  
        if i >=word_len and dp[i-word_len] == 1 and S[i-word_len:i] == word:
            dp[i] =1
            break
            
print(dp[len(S)])