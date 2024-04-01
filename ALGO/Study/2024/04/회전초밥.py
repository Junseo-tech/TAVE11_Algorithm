import sys
from itertools import combinations
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))

