import sys
import heapq

N = int(sys.stdin.readline())

heapmax =[]
heapmin =[]

for i in range(N):
    m = int(sys.stdin.readline().strip()) 
    
    # 최대힙부터 넣기 시작
    if len(heapmax) == len(heapmin):
        heapq.heappush(heapmax,-m)
    else:
        heapq.heappush(heapmin,m)

    if heapmin and -heapmax[0]>heapmin[0]:
        high = -heapq.heappop(heapmax)
        low = heapq.heappop(heapmin)
        heapq.heappush(heapmin, high)
        heapq.heappush(heapmax, -low)
    
    k = -heapmax[0]
    print(k)
        