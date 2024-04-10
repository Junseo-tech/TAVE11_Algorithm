import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
max_rupee = sys.maxsize

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y, visited):
    q = deque([])
    q.append((x,y))
    visited[x][y] = cave[x][y]

    while q:
        x,y = q.popleft()
        if x == N and y == N:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0 <= ny < N:
                if visited[nx][ny] > visited[x][y] + cave[nx][ny]:
                    visited[nx][ny] = visited[x][y] + cave[nx][ny]
                    q.append((nx,ny))

count = 0
while True:
    N = int(input())
    if N == 0:
        exit()
    cave = [list(map(int, input().split())) for _ in range(N)]
    visited = [[max_rupee] * N for _ in range(N)]
    bfs(0,0,visited)
    count += 1
    print(f"Problem {count}: {visited[N-1][N-1]}")

