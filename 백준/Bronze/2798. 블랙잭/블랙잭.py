import sys

f_input = list(map(int,sys.stdin.readline().split()))
cards = list(map(int,sys.stdin.readline().split()))

## 5 21
## 5 6 7 8 9

# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.


# N는 뽑은카드수, M은 수의합, arr는 카드리스트
def Nfor(arr,M): #3개뽑기에 3중포문으로만 가능함 왜냐면 첫번째 그리고 그다음인덱스 그리고 그다음인덱스 이런식으로 모든경우를 구하기때문
    max =0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1, len(arr)):
                sum = arr[i]+arr[j]+arr[k]
                if sum<=M and sum>max:  # M보다는 작고 + max보다는 커야 계속 더 큰값이 들어감
                    max = sum
    return max
                                
k =Nfor(cards,f_input[1])
print(k)