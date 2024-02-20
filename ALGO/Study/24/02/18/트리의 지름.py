import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
## 트리의 지름 : 트리에 존재하는 모든 경로중에 가장 긴 것
## 시작 노드 -> 가장 먼 곳 (weight 가장 큰 곳) 한 번 dfs
## 위에서 구한 해당 노드 -> 가장 먼 곳 ## dfs 두 번
## 위와 같이 구하면 지름 구하기 가능

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

visited = [-1] * (n+1)

def dfs(v,w):
    for i in graph[v]:
        child, weight = i
        if visited[child] == -1:
            visited[child] = w + weight
            dfs(child, w+weight)

dfs(1,0)
visited[1] = 0 # 여기에 정의 해주는 이유는 dfs 내부에 정의하면 weight가 안쌓이기 때문

start = visited.index(max(visited))
visited = [-1] * (n+1) # 배열 초기화
visited[start] = 0
dfs(start,0)

print(max(visited))