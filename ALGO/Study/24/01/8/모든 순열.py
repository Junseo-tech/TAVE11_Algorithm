import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
nums = []

for i in range(1,N+1):
    nums.append(i)

for per in permutations(nums):
    print(" ".join(map(str, per)))