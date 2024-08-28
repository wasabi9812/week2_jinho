import sys
import heapq
N = int(sys.stdin.readline().strip())
q = []
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    heapq.heappush(q,n)
    
result =[]

for i in range(N):
    min_rope = heapq.heappop(q)
    result.append(min_rope*(N-i))
    
print(max(result))