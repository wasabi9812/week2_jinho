import sys

N = int(input())

data = []
for i in range(N):
    M = int(input())
    data.append(M)

for j in range(len(data)-1):  # -1이유 정렬되면 마지막은 할필요없음
    min =j   
    for k in range(j+1,len(data)): # 모든문 돌면서 최소값 찾기
        if data[k]<data[min]:
            min = k
    data[j], data[min] = data[min], data[j]

for num in data:
    print(num)