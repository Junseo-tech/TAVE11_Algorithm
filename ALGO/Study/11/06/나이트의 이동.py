'''
체스판 위에 한 나이트가 놓여져 있다. 
나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
나이트가 이동하려고 하는 칸이 주어진다. 
나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력
----
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
각 테스트 케이스는 세 줄로 이루어져 있다. 
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
체스판의 크기는 l × l이다. 
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다.
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
----
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

예제 입력1
--------
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1

예제 출력1
--------
5
28
0

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import deque

T = int(input())

dx = [-2,-1,-2,-1,+2,+1,+2,+1]
dy = [+1,+2,-1,-2,+1,+2,-1,-2]

def bfs(x,y):
    visited[x][y] = True
    q = deque([(x, y, 0)])

    while q:
        x,y,depth = q.popleft()
        if x == goal_x and y == goal_y:
            return depth
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0<= ny < l:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx,ny, depth + 1))

for _ in range(T):
    l = int(input())
    visited = [[False] * l for _ in range(l)]
    present_x,present_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    print(bfs(present_x,present_y))
    
    

    

