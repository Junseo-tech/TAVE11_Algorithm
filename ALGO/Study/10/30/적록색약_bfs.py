import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
visited = [[False] * (N+1) for _ in range(N+1)]
q = deque()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

color_blindness = 0
normal = 0

def bfs(x,y):
    q.append((x,y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        cur_color = graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == False:
                    if graph[nx][ny] == cur_color:
                        bfs(nx,ny)

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i,j)
            normal += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i,j)
            color_blindness += 1

print(normal, color_blindness)