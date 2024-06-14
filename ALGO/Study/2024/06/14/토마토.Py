import sys
from collections import deque
input = sys.stdin.readline
M,N = map(int, input().split()) # M : 가로, N : 세로
tomatos = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
# -1 : 토마토 안들어 있음 , 1 : 익은 토마토, 0 : 익지 않은 토마토

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while q:
        x,y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if tomatos[nx][ny] == 0:
                    tomatos[nx][ny] = tomatos[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx,ny))

q = deque()
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == -1:
            visited[i][j] = True
        if tomatos[i][j] == 1:
            q.append((i,j))

bfs()

max_count = 0
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 0:
            print(-1)
            exit()
        max_count = max(max_count, tomatos[i][j])

print(max_count-1)