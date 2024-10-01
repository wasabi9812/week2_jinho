import sys

N = int(sys.stdin.readline())

table = {}

# 키는 카드종류
# 밸류는 

for i in range(N):
    k = int(sys.stdin.readline())
    if k in table:
        table[k] +=1
    else:
        table[k] =1
    

max = 0   
maxkey = 0
for key in table:
    if table[key]>max:
        max = table[key]
        maxkey = key
    elif table[key] == max:
        if key>maxkey:
            maxkey = maxkey
        if key<maxkey:
            maxkey = key
            
print(maxkey)