import sys
import heapq
N = int(sys.stdin.readline().strip())
minheap = []

for i in range(N):
    M = int(sys.stdin.readline().strip())
    heapq.heappush(minheap,M)

#누적
heapsum = 0


while len(minheap)>1:
    q1 = heapq.heappop(minheap)
    q2 = heapq.heappop(minheap)
    q3 = q1+q2
    heapsum +=q3
    heapq.heappush(minheap, q3)
print(heapsum)