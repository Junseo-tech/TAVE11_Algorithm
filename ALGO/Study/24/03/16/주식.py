import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    max_price = 0
    money = 0
    for i in range(N-1,-1,-1):
        if stock[i] > max_price:
            max_price = stock[i]
        money += max_price - stock[i]
    print(money)