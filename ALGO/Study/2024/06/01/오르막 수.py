N = int(input()) # 수의 길이
dp = [0 for _ in range(1001)]
MOD = 10007
# 수는 0 으로 시작할 수 있다
# 인접한 수가 같아도 오름차순이다

dp[1] = 10 % 10007
dp[2] = 55 % 10007

for i in range(3, 1001):
    sum = 0
    for j in range(10, -1, -1):
        print("j", j)
        #print("dp[i-1] - j : " , (dp[i-1] - j) % MOD)
        sum += dp[i-1] - j
        print(sum)
    dp[i] = sum % MOD

#print(dp)