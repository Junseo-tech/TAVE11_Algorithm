import sys
from functools import cmp_to_key
input = sys.stdin.readline
N = int(input())
calendar = []

for _ in range(N):
    S,E = map(int, input().split())
    calendar.append((S,E))

calendar.sort(key=cmp_to_key(lambda x,y : -1 if x[0] == y[0] and x[1]-x[0] > y[1]-y[0] else 1))

schedule = [0 for _ in range(367)]
for x,y in calendar:
    for i in range(x,y+1):
        if schedule[i] == 0:
            schedule[i] = 1
        else:
            schedule[i] += 1

width, height, area = 0,0,0
for i in range(len(schedule)):
    if schedule[i] != 0:
        width += 1
        height = max(height, schedule[i])
    else:
        area += width * height
        width, height = 0,0

print(area)