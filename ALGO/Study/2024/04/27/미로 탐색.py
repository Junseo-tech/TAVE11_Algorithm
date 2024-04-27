import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N,M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
INF = sys.maxsize
visited = [[INF] * (M) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(start, end):
    global dx, dy
    q = deque([(start, end)])
    visited[start][end] = min(visited[start][end], maze[start][end])
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0 <= ny < M and visited[nx][ny] > visited[x][y] + maze[nx][ny] : # 방문 체크 잊지 말기
                if maze[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = min(visited[nx][ny], visited[x][y] + maze[nx][ny])

bfs(0,0)
print(visited[N-1][M-1])