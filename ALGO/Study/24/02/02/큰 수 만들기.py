import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
number = [str(x) for x in numbers]
if all(i == '0' for i in number):
    print('0')
else:
    max_len = len(max(number, key = len))
    number = sorted(number, key = lambda x : x * max_len, reverse=True)
    print(''.join(map(str, number)))
