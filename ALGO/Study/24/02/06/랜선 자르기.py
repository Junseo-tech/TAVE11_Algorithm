import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))
lines.sort()

min = 0
max = len(lines) - 1
mid = (min + max) // 2
count = 0

while min < max :
    for line in lines:
        count += line // mid
    if count >= N :
        max -= 1
        mid = (min + max) // 2
    else:
        min += 1
        mid = (min + max) // 2
print(count)