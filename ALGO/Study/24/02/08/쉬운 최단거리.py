import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int, input().split())

visited = [[0] * m for _ in range(n)]
graph = []
for _  in range(m):
    graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and graph[nx][ny] >= 1:
                visited[nx][ny] += (visited[x][y] + 1)
                q.append((nx,ny))
    return

bfs(0,0)
for i in range(1,n):
    for j in range(1,m):
        if graph[i][j] == 2:
            bfs(i,j)
            break

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] != 0:
            print(-1, '', end = '')
        elif visited[i][j] and graph[i][j] >= 1:
            print(visited[i][j]-1, '' , end = '')
        else:
            print(visited[i][j], '' , end = '')
