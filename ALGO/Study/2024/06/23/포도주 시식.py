import sys
input = sys.stdin.readline
N = int(input())
# 3잔 연속으로 마실 수 없다
wine = [] # 6 10 13 9 8 1
for _ in range(N):
    w = int(input())
    wine.append(w)
count = 0

if N == 1:
    print(wine[0])
    exit()
dp = [0] * (N+1)

if N > 1:
    dp[0], dp[1], dp[2] = 0, wine[0], wine[0] + wine[1]
for i in range(3,N+1):
    # 연속으로 선택 되면 막아야 함 (3개)
    dp[i] = max(dp[i-1], dp[i-2] + wine[i-1], dp[i-3] + wine[i-2] + wine[i-1])
    
print(dp[N])

#dp[0] = 0, dp[1] = 6, dp[2] = 16
# 3번째꺼 선택 X 의 경우 : dp[2] = 16
# dp[1] + wine[2] : 맨 처음 6 + 현재 인덱스 13 = 19
# dp[0] + wine[1] + wine[2] : 현재 잔 + 직전 잔 + 3번째 전 잔 X