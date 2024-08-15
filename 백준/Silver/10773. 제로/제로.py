import sys

# class FixedStack:
    
#fixed리스트 구현 안하고

# #==============================


N = int(sys.stdin.readline().strip())
M = [int(sys.stdin.readline()) for _ in range(N)]


stacklist = []
for i in range(len(M)):
    if M[i]==0:
        stacklist.pop()
    else:
        stacklist.append(M[i])

stacksum =0
for i in stacklist:
    stacksum += i
    
print(stacksum)