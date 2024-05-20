import sys
from collections import deque
input = sys.stdin.readline
M,N,H = map(int, input().split()) # M : 가로, N : 세로, H : 높이
tomatos = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * (M) for _ in range(N)] for _ in range(H)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while q:
        z,y,x = q.popleft()
        visited[z][y][x] = True
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<M and 0<=ny<N and 0<=nz<H and not visited[nz][ny][nx]:
                if tomatos[nz][ny][nx] == 0:
                    tomatos[nz][ny][nx] = tomatos[z][y][x] + 1
                    q.append((nz,ny,nx))
                    visited[nz][ny][nx] = True

q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 1:
                q.append((i,j,k))
            if tomatos[i][j][k] == -1:
                visited[i][j][k] = True

bfs()

max_count = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 0:
                print(-1)
                exit()
            max_count = max(max_count, tomatos[i][j][k])

print(max_count-1)
