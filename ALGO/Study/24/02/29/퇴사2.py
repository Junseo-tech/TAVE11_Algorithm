import sys
input = sys.stdin.readline
N = int(input())
work = [list(map(int, input().split())) for _ in range(N)] + [[0,0]] + [[0,0]]
dp = [0] * (N + 2)
max_num = -1
for i in range(N+1):
    if max_num < dp[i]:
        max_num = dp[i]
    nxt = i + work[i][0]
    if nxt < N+2:
        dp[nxt] = max(dp[nxt], max_num + work[i][1])

print(dp[N])