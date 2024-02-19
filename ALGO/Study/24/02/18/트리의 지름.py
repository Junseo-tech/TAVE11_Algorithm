import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    parent,child,weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

visited = [False] * (n+1)

global count
def dfs(v):
    visited[v] = True
    count = 0
    for i in graph[v]:
        child, weight = i
        if not visited[child]:
            dfs(child)
            count += weight
    return count
            
print(dfs(1))