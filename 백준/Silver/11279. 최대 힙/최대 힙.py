import sys, heapq

input = sys.stdin.readline
N = int(input())
q = []

for i in range(N):
    m = int(input())
    if m !=0:
        heapq.heappush(q,-m)
    elif m == 0:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)
    
    