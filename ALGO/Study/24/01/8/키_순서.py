import sys
input = sys.stdin.readline

N,M = map(int, input().split())
upper = [[] for _ in range(N+1)]
down =[[] for _ in range(N+1)]

# graph 방향 설정
for _ in range(M):
    a,b = map(int, input().split())
    upper[a] += [b]
    down[b] += [a]
    # = 라고 하면 대입되어 뒤에 들어오는 것으로 갱신 됨. + 해줘야함

# dfs 정의
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

count = 0
for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(upper,1,visited)
    dfs(down,1,visited)

    if sum(visited) == N: #True를 합산 함
        count += 1

print(count)

