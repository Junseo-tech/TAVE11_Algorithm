import sys
input = sys.stdin.readline
from collections import deque

# 백 트래킹 -> 모든 경우의 수를 탐색하는데 불가능 하면 백
N = int(input())
graph = [list(map(str, input().strip().split())) for _ in range(N)]
teacher = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            teacher.append((i,j))

flag = False
# 장애물 설치 -> 모든 경우의 수 
def set_obstacle(obstacle):
    global flag
    if obstacle == 3:
        if bfs():
            flag = True
            return
    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    set_obstacle(obstacle + 1)
                    graph[i][j] = 'X'


dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 탐색하면서 될 지 아닐 지 확인하기
def bfs():
    for t in teacher:
        x, y = t
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < N and 0<= ny < N:
                if graph[nx][ny] == 'S':
                    return False
                if graph[nx][ny] == 'O':
                    break # while문 벗어나서 다음 for문으로
                nx += dx[i]
                ny += dy[i]
    return True
                

set_obstacle(0)

if flag:
    print("YES")
if not flag:
    print("NO")