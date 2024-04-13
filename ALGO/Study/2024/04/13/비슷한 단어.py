import sys
from itertools import product
input = sys.stdin.readline
N = int(input())
words = []

for _ in range(N):
    words.append(input().strip())

s = words[0]
count = 0
max_length = max(len(word) for word in words[1:])

candidate_list = []

for i in range(1, max_length+1): 
    for p in product(s , repeat = 1):
        candidate = ''.join(map(str, p))
        candidate_list.append(candidate)

for i in words[1:]:
    for j in candidate_list:
        if i == j:
            count += 1

print(count)
