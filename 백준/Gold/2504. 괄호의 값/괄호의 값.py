import sys
S = sys.stdin.readline().strip()

stack = []
temp =1
result = 0

for i in range(len(S)):
    if S[i] == "(":
        stack.append("(")
        temp *=2    
    elif S[i] == "[":
        stack.append("[")
        temp *=3
        
    elif S[i] == ")":  #닫을때 )
        if not stack or stack[-1] =="[":
            result = 0
            break
        if S[i-1] =="(":
            result += temp
        stack.pop()
        temp//=2
    else: # 닫을때 ]
        if not stack or stack[-1] =="(":
            result =0
            break
        if S[i-1] =='[':
            result+=temp
        stack.pop()
        temp//=3

if stack:
    print(0)
else:
    print(result)