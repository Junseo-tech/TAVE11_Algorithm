import sys
input = sys.stdin.readline
from itertools import combinations

N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append([i,j])
        if graph[i][j] == 1:
            house.append([i,j])

result = sys.maxsize
for comb in combinations(chicken, M):
    temp = 0
    for r,c in house:
        dist = sys.maxsize
        for x,y in comb:
            dist = min(dist, abs(r-x) + abs(c-y))
        temp += dist
    result = min(result, temp)

print(result)


