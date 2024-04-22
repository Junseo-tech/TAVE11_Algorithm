import sys
input = sys.stdin.readline
from copy import deepcopy
from collections import deque
N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def makewall(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makewall(count+1)
                graph[i][j] = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

def bfs():
    global dx, dy
    tmp_graph = deepcopy(graph)
    q = deque([])
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                q.append((i,j))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    q.append((nx,ny))
            else:
                continue
    count = 0
    global answer

    for i in range(N):
        count += tmp_graph[i].count(0)

    answer = max(answer, count)

makewall(0)
print(answer)