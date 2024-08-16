import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())

queue = deque([i for i in range(1, N+1)])
result = []


while len(queue)>0:
        for i in range(K-1):
            n1 = queue.popleft()
            queue.append(n1)
            
        n2 = queue.popleft()
        result.append(n2)


print("<"+", ".join(map(str,result))+">")
