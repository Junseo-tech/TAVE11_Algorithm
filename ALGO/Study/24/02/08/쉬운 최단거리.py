import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
loads = []
visited = [[0] * m for _ in range(n)]

nx = [-1,1,0,0]
ny = [0,0,-1,1]

for _ in range(m):
    loads.append(input().split())

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        if loads[x][y] == 2:
            visited[x][y] = 1
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if loads[dx][dy] == 2:
                visited[dx][dy] += 1
            else:
                if not visited[dx][dy]:
                    visited[dx][dy] = 1
                    q.append((dx,dy))
bfs(0,0)

print(visited)