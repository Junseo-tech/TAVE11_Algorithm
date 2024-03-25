import sys
from collections import deque
input = sys.stdin.readline
N,M,V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (N+1)
visited2 = [False] * (N+1)

def dfs(start, visited):
    print(start, end = " ")
    visited[start] = True
    graph[start].sort()
    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited)

def bfs(start, visited2):
    q = deque([start])
    visited2[start] = True
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in graph[v]:
            graph[v].sort()
            if not visited2[i]:
                q.append(i)
                visited2[i] = True
dfs(V, visited)
print( )
bfs(V, visited2)

