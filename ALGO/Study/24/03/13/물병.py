import sys
input = sys.stdin.readline
N,K = map(int,input().split())

answer = 0

while bin(N).count('1') > K:
    answer += N & -N
    N += N & -N

print(answer)


