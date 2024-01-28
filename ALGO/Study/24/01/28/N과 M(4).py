import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
nums = []

for i in range(1,N+1):
    nums.append(i)

result = list(combinations_with_replacement(nums, M))
result_str = '\n'.join([' '.join(map(str, comb)) for comb in result])

print(result_str)
    