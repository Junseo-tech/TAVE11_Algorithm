import sys
input = sys.stdin.readline
from itertools import permutations
N, K = map(int, input().split())
A = list(map(int, input().split()))
present_weight = 500
count = 0

for per in permutations(A, N):
    weight = 0
    now = 0
    for i in range(N):
        weight = weight + per[i] - K
        if present_weight + weight < present_weight:
            break
        else:
            now += 1
    if now == len(per):
        count += 1
            

print(count)

    


