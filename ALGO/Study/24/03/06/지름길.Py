import sys
input = sys.stdin.readline
N,D = map(int, input().split())
load = [list(map(int, input().split())) for _ in range(N)] + [[0,0,0]]
dp = [0] * (D+1)
max_num = 0
for i in range(N+1):
    start, destination, shortest = load[i]
    origin = destination - start
    


