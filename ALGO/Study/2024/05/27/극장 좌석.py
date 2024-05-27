import sys
input = sys.stdin.readline
N = int(input())
M = int(input()) # 고정석의 갯수

fix = []
dp = [1 for _ in range(N+1)]
for _ in range(M):
    num = int(input())
    fix.append(num)

answer = 1


for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]


# for i in range(2, N+1):
#     if i not in fix:
#         dp[i] = dp[i-1] + dp[i-2]
# 아래에서 거르니까 건너 뛰면 안됨. 건너 뛰어서 계산하면 수가 커졌을 때 문제 발생할 수 있다

fixed = 0
# 4, 7
if M > 0:
    for seat in fix:
        if seat - fixed - 1 > 0:
            answer *= dp[seat-fixed-1]
        fixed = seat
    if N - fixed > 0:
        answer *= dp[N-fixed]
else:
    answer = dp[N]

#print(dp)
print(answer)