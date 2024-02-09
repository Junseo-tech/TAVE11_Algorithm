import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
numbers= list((map(int, input().split())))
count = 0
for i in range(1, len(numbers)+1):
    for comb in combinations(numbers, i):
        if int(sum(comb)) == S:
            count += 1
print(count)