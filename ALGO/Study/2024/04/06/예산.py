import sys
input = sys.stdin.readline

N = int(input())
budget = list(map(int, input().split()))
total_budget = int(input())
budget.sort()

left = 0
right = max(budget)


while left <= right:
    answer = 0
    mid = (left + right) // 2
    for money in budget:
        if money > mid:
            money = mid
        answer += money
    if answer > total_budget:
        right = mid - 1
    else: # answer가 클 때 
        left = mid + 1

print(right)
