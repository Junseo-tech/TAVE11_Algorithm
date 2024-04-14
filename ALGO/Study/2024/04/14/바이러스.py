import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**9)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x , y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N+1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

bfs(1)
answer = visited.count(True)
print(answer - 1)

    