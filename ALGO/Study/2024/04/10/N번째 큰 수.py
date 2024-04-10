import sys
import heapq
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
max_heap = []

for i in range(N):
    for j in range(N):
        heapq.heappush(max_heap, data[i][j])
        if len(max_heap) > N:
            heapq.heappop(max_heap)

print(heapq.heappop(max_heap))