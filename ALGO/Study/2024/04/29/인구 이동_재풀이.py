import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

N,L,R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,visited):
    q = deque([(x,y)])
    union = [(x,y)]
    visited[x][y] = True
    count = people[x][y]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if L <= abs(people[x][y] - people[nx][ny]) <= R:
                    union.append((nx,ny))
                    count += people[nx][ny]
                    q.append((nx,ny))
                    visited[nx][ny] = True
            
    return union, count // len(union)

def move():
    flag = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union, count = bfs(i,j,visited)
                if len(union) > 1:
                    flag = True
                    for x,y in union:
                        people[x][y] = count
    return flag

answer = 0
while move():
    answer += 1

print(answer)