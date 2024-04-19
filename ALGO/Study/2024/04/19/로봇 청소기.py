import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
r,c,d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def isExist(x,y):
    global dx, dy
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<=ny<M and graph[nx][ny] == 0:
            return True
    return False
 
while True:
    graph[r][c] = 2
    if isExist(r,c):
        while True:
            d = (d+3) % 4
            if graph[r + dx[d]][c + dy[d]] == 0:
                r += dx[d]
                c += dy[d]
                break
    else:
        if graph[r - dx[d]][c - dy[d]] == 1:
            break
        else:
            r -= dx[d]
            c -= dy[d]

result = 0
for i in graph:
    result += i.count(2)

print(result)