import sys
input = sys.stdin.readline
N,K = map(int,input().split())

answer = 0
print(bin(N))
while bin(N).count('1') > K:
    N += 1
    answer += 1

print(answer)