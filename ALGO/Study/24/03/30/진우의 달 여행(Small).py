import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
direction = [-1,0,1]

def dfs(x,y,dir,min_num,answer):
    if x == N-1:
        return min(min_num, answer)
    for i in direction:
        if i != dir:
            if 0 <= x < N and 0<= y+i < M:
                min_num = dfs(x+1,y+i,i,min_num,answer + space[x+1][y+i])
    return min_num
min_num = int(sys.maxsize)
for i in range(M):
    min_num = min(min_num, dfs(0,i,2,min_num,space[0][i]))

print(min_num)
