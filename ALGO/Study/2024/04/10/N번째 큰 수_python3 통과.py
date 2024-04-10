import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        # heapq.heappush(max_heap, num)
        if len(heap) < N:
            heapq.heappush(heap, num)
        if heap[0] < num:
            heapq.heappushpop(heap, num)

print(heapq.heappop(heap))
            
