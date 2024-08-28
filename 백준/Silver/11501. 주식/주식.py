import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):


    N = int(sys.stdin.readline().strip())

    stocks =list(map(int,sys.stdin.readline().split()))
    
    max = 0
    reversedsum =0
    for i in range(N-1,-1,-1):
        if stocks[i]>max: #최대값 갱신
            max=stocks[i]
        reversedsum+=max-stocks[i]

    print(reversedsum)