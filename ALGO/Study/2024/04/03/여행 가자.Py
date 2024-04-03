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

def bfs(start, route, graph):
    q = deque([])
    q.append(start)
    if len(route) == 0:
        print("YES")
        return
    while q:
        now = q.popleft() # 1, 2
        print("now", now)
        next = route.popleft() # 2, 3, 3
        if len(route) == 0: # 3, 2
            print("YES")
            return
        for i in graph[now]:
            if i == next:
                q.append(next) # 2
                print("q에 추가 되는 next 출력 : ",i, next) # 2 일 때 next로 2
            else:
                route.appendleft(next)
                
                print("루트에 추가 되는 next 출력: " , i, next) # next로 3이 다시 추가
    print("NO")
    return


bfs(route.popleft(), route, graph)




