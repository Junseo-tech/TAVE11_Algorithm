# 길이 있으면, 즉 무한대가 아니면 count += 1
import sys
input = sys.stdin.readline
MAX = int(1e9)

N,M = map(int, input().split())
graph = [[MAX for j in range(N+1)] for i in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer = 0
for i in range(1,N+1):
    count = 0
    for j in range(1,N+1):
        if graph[i][j] != MAX or graph[j][i] != MAX: 
            count += 1
    if count == N-1: #N-1인 이유 : N이면 자기 자신에서 자기 자신인 것 까지 포함해야 함
        answer += 1
print(answer)