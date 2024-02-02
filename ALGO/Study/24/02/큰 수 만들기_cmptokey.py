import sys
from functools import cmp_to_key
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
numbers = [str(x) for x in numbers]
numbers.sort(key = cmp_to_key(lambda x,y : -1 if (x+y) > (y+x) else 1))
answer = ''.join(numbers)
print(int(answer))