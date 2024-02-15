import sys
from collections import deque
input = sys.stdin.readline

# N은 세로 M은 가로 N개의 줄에 M개의 숫자
N,M = map(int, input().split(" "))

graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    visited[x][y] = 1
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if graph[nx][ny] == 0 :
                    visited[nx][ny] = 0
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

                
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2 and visited[i][j] == 0:
            bfs(i,j)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end = ' ')
        else:
            print(visited[i][j]-1, end = ' ')
    print()