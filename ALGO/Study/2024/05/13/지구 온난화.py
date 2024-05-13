import sys
from collections import deque
import copy

input = sys.stdin.readline
R,C = map(int, input().split())
maps = [list(input().strip()) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

answer = copy.deepcopy(maps)

for y in range(R):
    for x in range(C):
        count = 0
        if maps[y][x] == '.':
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx< C and 0<=ny<R:
                if maps[ny][nx] == '.':
                    count += 1
            else:
                count += 1
        if count >= 3:
            answer[y][x] = '.'

start,end = 0,0
for i in range(R):
    if 'X' in answer[i]:
        start = i
        break
for i in range(R-1,-1,-1):
    if 'X' in answer[i]:
        end = i
        break

tmp = []
for j in range(C):
    for i in range(start, end+1):
        if 'X' == answer[i][j]:
            tmp.append(j)
            break

for i in range(start, end+1):
    print("".join(answer[i][tmp[0]:tmp[-1]+1]))

