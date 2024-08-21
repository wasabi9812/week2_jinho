import sys, heapq

input = sys.stdin.readline
N = int(input())

minq = []

for i in range(N):
    m = int(input())
    heapq.heappush(minq,m)
    
result =0
    
while len(minq)>1:
    k1 = heapq.heappop(minq)
    k2 = heapq.heappop(minq)
    k3 = k1+k2
    result += k3
    heapq.heappush(minq,k3)
    

print(result)