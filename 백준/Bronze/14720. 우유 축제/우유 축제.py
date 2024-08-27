import sys
N = int(sys.stdin.readline().strip())
data = list(map(int,sys.stdin.readline().split()))

milk = 0
cnt = 0
for i in range(N):
    kind = milk%3
    if data[i]==kind:
        milk+=1
        cnt+=1
    else:
        continue  
print(cnt)
