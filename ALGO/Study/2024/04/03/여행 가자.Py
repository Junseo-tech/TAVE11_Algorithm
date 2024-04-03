import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) #도시의 수
M = int(input()) #여행 계획에 속한 도시의 수 
linked_city = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N+1)]
route = deque(list(map(int, input().split())))

# 도시 연결 관계 그래프 생성
for i in range(N):
    for j in range(N):
        if linked_city[i][j] == 1:
            graph[i+1].append(j+1)

def bfs(start, next): 
    q = deque([start])
    visited = [False] * (N+1)
    visited[start] = True
    while q:
        now = q.popleft() 
        if now == next:
            return True
        for i in graph[now]: 
            if not visited[i]:
                visited[i] = True 
                q.append(i) 
    return False

answer = True
for i in range(M-1):
    if not bfs(route[i], route[i+1]):
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")