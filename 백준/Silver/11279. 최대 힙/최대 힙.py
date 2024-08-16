import sys
import heapq

N = int(sys.stdin.readline())

heap =[]

for i in range(N):
    m = int(sys.stdin.readline().strip())
    if m ==0:
        if heap:
            print(-(heapq.heappop(heap)))
        else:
            print(0)
    else:    
        heapq.heappush(heap,-m)
    
