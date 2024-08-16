import sys
from collections import deque

N = int(sys.stdin.readline().strip())

queue = deque([i for i in range(1, N+1)])

while len(queue)>1:
    queue.popleft()
    n = queue.popleft()
    queue.append(n)
    
print(queue[0])