import sys

N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append((sys.stdin.readline().strip()))
    

def successive(string):
    cnt = 0
    sum = 0
    result = 0
    for char in string:
        if char == "O":
            cnt += 1
            sum = cnt
            result += sum
        else:
            cnt = 0
            sum = 0
    return result

for test_case in data:
    print(successive(test_case))