import sys
from collections import deque
input = sys.stdin.readline
R,C = map(int, input().split())
maps = [list(input().strip()) for _ in range(R)]
gpses = []
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'X':
            gpses.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque([(x,y)])
    visited = [[False] * C for _ in range(R)] 
    visited[x][y] = True
    count = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<C and 0<=ny<R:
                if maps[nx][ny] == '.':
                    count += 1
            else:
                count += 1
                continue
    return count

for x,y in gpses:
    count = bfs(x,y)
    if count >= 3:
        pass
    else:
        pass
    
                
    

