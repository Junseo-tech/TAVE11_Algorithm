import sys
input = sys.stdin.readline

day = int(input())
ti = [0] * (day+1)
pi = [0] * (day+1)
dp = [0] * (day + 1)
save = 0

for i in range(day):
    ti[i], pi[i] = map(int, input().split())

for i in range(day):
    if save < dp[i]:
        save = dp[i]
        # print(save, i)
    if i + ti[i] < day + 1: 
        dp[i + ti[i]] = max(dp[i + ti[i]], save + pi[i])


print(dp[day])