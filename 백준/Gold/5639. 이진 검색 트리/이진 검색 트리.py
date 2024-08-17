import sys
sys.setrecursionlimit(10**6)
data = []
for line in sys.stdin:
    num = int(line.strip())
    if 0 < num < 1000000:  # 106보다 작은 양의 정수 조건 확인
        data.append(num)
        
origin=[]
def binary_tree(root,arr):
    templeft =[]
    tempright=[]
    if len(arr)==1:
        origin.append(root)
        return
    for i in range(1,len(arr)):
        if root>arr[i]:
            templeft.append(arr[i])
        else:
            tempright.append(arr[i])
           
    if templeft:
        binary_tree(templeft[0], templeft)
    if tempright:
        binary_tree(tempright[0], tempright)
    origin.append(root) 

binary_tree(data[0],data)
for i in origin:
    print(i)