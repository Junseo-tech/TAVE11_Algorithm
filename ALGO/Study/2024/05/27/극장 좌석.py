import sys
input = sys.stdin.readline
N = int(input())
M = int(input()) # 고정석의 갯수

fix = [False for _ in range(N+1)]
dp = [1 for _ in range(N+1)]
for _ in range(M):
    num = int(input())
    fix[num] = True
# 바로 왼, 오른쪽 자리에 고정석이 있는 것들
# 앞에가 정해지면 뒤에도 정해진다. 

dp[0], dp[1] = 1, 1
answer = 1

for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
                   
if M > 0:
    pass
else:
    answer = dp[N-1]
print(dp)
print(answer)