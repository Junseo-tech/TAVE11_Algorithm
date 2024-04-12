import sys
input = sys.stdin.readline
from itertools import permutations
S = input().strip()
zero = 0
one = 0
answer = []
for i in S:
    if i == "0":
        zero += 1
    else:
        one += 1

zero_half = zero // 2
one_half = one // 2

for i in S:
    if i == "0" and zero_half != 0:
        answer.append(i)
        zero_half -= 1
    if i == "1" and one_half != 0:
        one_half -= 1
        answer.append(i)

answer.sort()
print(''.join(map(str, answer)))

