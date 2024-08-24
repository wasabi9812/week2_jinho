import sys

case , target = map(int,sys.stdin.readline().split())

coins = []
count = 0

for i in range(case):
    n = int(sys.stdin.readline().strip())
    coins.append(n)
    
coins.sort(reverse=True)

for coin in coins:
    if target>=coin:
        count += target//coin
        target %= coin
    
print(count)