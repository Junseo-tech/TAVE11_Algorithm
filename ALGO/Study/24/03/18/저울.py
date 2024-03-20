import sys
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j :
            graph[i][j] = 0

for _ in range(M):
    heavy, light = map(int, input().split())
    graph[heavy][light] = 1

#플로이드 와셜 점화식 - a애서 b로 가는 경로가 있는지 확인
for k in range(1,N+1):
    for i in range(1,N+1): 
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,N+1):
    count = 0
    for j in range(1,N+1):
        if graph[i][j] == INF and graph[j][i] == INF: # a > b, b > a 가는 경우가 없는경우
            count += 1
    print(count)

