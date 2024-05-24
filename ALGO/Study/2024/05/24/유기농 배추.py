import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and space[nx][ny] == 1:
                    q.append((nx,ny))
                    visited[nx][ny] = True

answer = []
for _ in range(T):
    bug = 0
    M, N, K = map(int, input().split()) #M : 가로, N: 세로, K : 배추 위치의 개수
    space = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        y,x = map(int,input().split())
        space[x][y] = 1

    for i in range(N):
        for j in range(M):
            if space[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                bug += 1
    
    answer.append(bug)

for i in range(len(answer)):
    print(answer[i])

    
                
