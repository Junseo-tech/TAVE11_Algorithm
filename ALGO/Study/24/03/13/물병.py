import sys
input = sys.stdin.readline
N,K = map(int,input().split())

answer = 0

while bin(N).count('1') > K:
    N += (N & -N)
    answer += (N & -N)

print(answer)