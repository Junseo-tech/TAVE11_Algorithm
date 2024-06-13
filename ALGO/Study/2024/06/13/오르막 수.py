N = int(input())
MOD = 10007

dp = [1 for _ in range(10)] # 00 01 11 12

for i in range(N-1):
    for j in range(10):
        dp[j] = sum(dp[j:])

print(sum(dp)%MOD)