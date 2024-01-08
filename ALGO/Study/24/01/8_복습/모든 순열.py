import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
pers = permutations([i for i in range(1,N+1)], N)
for p in pers:
    answer = list(p)
    print(*answer)