# 피보나치 수열 함수의 호출 횟수 구하기
n = int(input())
dp = [0] * 51
dp[0] = dp[1] = 1
for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007
print(dp[n])
