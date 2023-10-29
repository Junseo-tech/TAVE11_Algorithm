'''
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 
따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. 
(색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. 
(빨강 2, 파랑 1, 초록 1)
하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. 
(빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 
적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
----
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
----
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

예제 입력 1
---------
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

예제 출력 1
---------
4 3

'''
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
visited = [[False] * (N+1) for _ in range(N+1)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

color_blindness = 0
normal = 0

def dfs(x,y):
    visited[x][y] = True
    cur_color = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == False:
                if graph[nx][ny] == cur_color:
                    dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            normal += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            color_blindness += 1

print(normal, color_blindness)

