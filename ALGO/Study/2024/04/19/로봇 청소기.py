import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
r,c,d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * (M+1) for _ in range(N)]

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def isExist(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

count = 0
while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        count += 1
    if isExist(r,c):
        pass
    else:
        pass
