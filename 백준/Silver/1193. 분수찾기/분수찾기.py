import sys

N = int(sys.stdin.readline())

numerator = 0 # 분자 y
denominator = 0 # 분모 x

# 1: 0,0
# 2: 1,0
# 3: 0,1
# 4: 2,0
# 5: 1,1
# 6: 0,2
# 7: 3,0
# 8: 2,1
# 9: 1,2
# 10: 0,3


# 1 2 4 7 11 fibo
# 3 5 8 12
linesum = 0
temp = 0
line =0
while(linesum<N):
    temp+=1
    linesum+=temp
    line +=1
    
# print(linesum)
# print(temp)
# print(line)
first_index = 0
last_index =0
for i in range(1,line):
    first_index+=i
# print(first_index)
last_index =0
for i in range(1, line+1):
    last_index+=i
# print(last_index)

#ex N=7 line=4 first_index=6
if line%2 ==0: #짝수일때
    numerator =1 # 분자 y
    denominator = line # 분모 x
    for i in range(first_index,last_index+1):
        if i == N-1: # 해당숫자라면
            break
        else:
            numerator+=1
            denominator-=1
else: #홀수일때
    numerator =line # 분자 y
    denominator = 1 # 분모 x
    for i in range(first_index,last_index+1):
        if i == N-1: # 해당숫자라면
            break
        else:
            numerator-=1
            denominator+=1
            
print(str(numerator)+"/"+str(denominator))