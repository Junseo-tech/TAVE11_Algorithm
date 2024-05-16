import sys
input = sys.stdin.readline
N = int(input())
route = input().strip()
sub = 'EW'
count = 0
for i in range(1, N):
    if route[i-1] + route[i] == sub:
        count += 1

print(count)