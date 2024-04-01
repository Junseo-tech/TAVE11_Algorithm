import sys
input = sys.stdin.readline
N,M = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'), float('inf'), float('inf')] for _ in range(M)] for _ in range(N)]

for i in range(1,N+1):
    for j in range(M):
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + space[i-1][j]
        elif j < M-1:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + space[i-1][j]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + space[i-1][j]
        

min_value = float('inf')
for row in dp[i]:
    for each in row:
        min_value = min(min_value, each)
print(min_value)
            

