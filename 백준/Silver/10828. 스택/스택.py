import sys

N = int(sys.stdin.readline().strip())
stackinput = []
for i in range(N):
    M = list(map(str,sys.stdin.readline().split()))
    stackinput.append(M)

# for i in stackinput:
#     print(i)
    
    
class FixedStack:
    def __init__(self, capacity):
        self.capacity = capacity  # 스택의 최대 크기
        self.stack = []  # 스택을 저장할 리스트
        self.size = 0  # 현재 스택에 있는 요소의 수
    
    def push(self, item):
        """스택에 아이템을 추가한다. 스택이 가득 차면 예외를 발생시킨다."""
        if self.size >= self.capacity:
            raise OverflowError("Stack is full")
        self.stack.append(item)
        self.size += 1
    
    def pop(self):
        """스택에서 아이템을 제거하고 반환한다. 스택이 비어 있으면 예외를 발생시킨다."""
        if self.size == 0:
            return -1
        self.size -= 1
        return self.stack.pop()
    
    def peek(self):
        """스택의 맨 위에 있는 아이템을 반환하지만 제거하지는 않는다."""
        if self.size == 0:
            return -1
        return self.stack[-1]
    
    def is_empty(self):
        """스택이 비어 있는지 확인한다."""
        return self.size == 0
    
    def is_full(self):
        """스택이 가득 찼는지 확인한다."""
        return self.size == self.capacity
    
    def __len__(self):
        """스택에 있는 요소의 수를 반환한다."""
        return self.size
#===================================================================================================
stack = FixedStack(10000)

# print(stackinput[0][1])

for i in range(len(stackinput)):
    command = stackinput[i][0]
    
    if command == "push":
        stack.push(stackinput[i][1])
    elif command == "top":
        print(stack.peek())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if stack.is_empty():
            print("1")
        else:
            print("0")
    else:
        n = stack.pop()
        print(n)