import sys
input = sys.stdin.readline
N,M = map(int, input().split())
upper = [[] for _ in range(N+1)]
down = [[] for _ in range(N+1)]
#자기보다 큰 학생, 작은 학생의 수를 합쳤을 때 전체 학생의 수와 같으면 전부 다 알 수 있는 것 이다.

for _ in range(M):
    a,b = map(int, input().split())
    upper[a] += [b] # a번째 보다 큰 것이 누구누구 있는지
    down[b] += [a] # b번째 보다 작은 것이 누구누구 있는지

def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

count = 0
for i in range(1,N+1):
    visited = [False] * (N+1)
    dfs(upper,i,visited)
    dfs(down,i,visited)
    if sum(visited) == N:
        count += 1

print(count)
