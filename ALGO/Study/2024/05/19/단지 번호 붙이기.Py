import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
towns = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque([(x,y)])
    count = 1
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and towns[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                count += 1
                q.append((nx, ny))
    answer.append(count)

answer = []
for i in range(N):
    for j in range(N):
        if towns[i][j] == 1 and visited[i][j] == False:
            bfs(i,j)

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])