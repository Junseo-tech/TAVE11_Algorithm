N = int(input())
MOD = 10007

dp = [1 for _ in range(10)] # 00 01 11 12

for i in range(N-1):
    for j in range(10):
        dp[j] = sum(dp[j:])  #길이가 2 dp[0] = 10 dp[1] =9 dp[2] = 8

print(sum(dp)%MOD)