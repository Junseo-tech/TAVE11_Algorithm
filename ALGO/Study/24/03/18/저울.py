import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
answer = []
for _ in range(M):
    heavy, light = map(int, input().split())
    graph[heavy].append(light)
    graph[light].append(heavy)
