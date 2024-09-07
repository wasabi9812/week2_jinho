import sys

N = int(sys.stdin.readline())
dough_cost , topping_cost = map(int,sys.stdin.readline().split())
dough_cal = int(sys.stdin.readline())
topping_cal = []
for i in range(N):
    topping_cal.append(int(sys.stdin.readline()))

topping_cal.sort(reverse=True)

cal = dough_cal
money = dough_cost
cal_per_cost = cal//money

for toppings in topping_cal:  
        cal += toppings
        money += topping_cost
        if cal_per_cost<cal//money:
            cal_per_cost = cal//money
            
print(cal_per_cost)