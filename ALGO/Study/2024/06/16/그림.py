import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split()) # N : 세로, M : 가로
picture = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]
ans = []
def bfs(x,y,count):
    q = deque([(x,y)])
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and picture[nx][ny] == 1 and not visited[nx][ny]:
                count += 1
                q.append((nx, ny))
                visited[nx][ny] = True
    return count
        

for i in range(N):
    for j in range(M):
        if picture[i][j] == 1 and not visited[i][j]:
            count = 1
            count = bfs(i,j,count)
            ans.append(count)


print(len(ans))
if len(ans) >= 1:
    print(max(ans))
    exit()
else:
    print(0)