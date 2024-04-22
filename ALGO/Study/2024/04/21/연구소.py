import sys
input = sys.stdin.readline
from itertools import combinations
from copy import deepcopy
from collections import deque

N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
blank = []
virus = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            blank.append([i,j])
        if graph[i][j] == 2:
            virus.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def diffuse(tmp_graph, virus):
    global dx, dy
    q = deque(virus)
    visited = [[False] * (M) for _ in range(N)]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0<= ny < M and not visited[nx][ny]:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    visited[nx][ny] = True
                    q.append((nx,ny))
                if tmp_graph[nx][ny] == 1:
                    continue
    return tmp_graph

max_count = -1
for comb in combinations(blank, 3):
    tmp_graph = deepcopy(graph)
    count = 0
    for x,y in comb:
        tmp_graph[x][y] = 1
    tmp_graph = diffuse(tmp_graph, virus)
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 0:
                count += 1
    max_count = max(max_count, count)


print(max_count)
                
