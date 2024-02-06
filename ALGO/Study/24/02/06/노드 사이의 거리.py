import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    point_1, point_2, weight = map(int, input().split())
    graph[point_1].append((point_2, weight))
    graph[point_2].append((point_1, weight))

visited = [False] * (N+1)

def bfs(x,y): # x -> 시작 y -> 끝
    q = deque([(x,y,0)]) # 시작점, 끝 점, weight
    visited = [False] * (N+1) # 1-> 2 -> 3이 첫번째 입력이고 1 -> 2 -> 4가 두번 째면 2가 방문 처리 되면 안됨. 호출 시 마다 초기화
    visited[x] = True
    while q:
        x,y, weight = q.popleft()
        if x == y :
            return weight
        for i in graph[x]:
            next_point, next_weight = i
            if not visited[next_point]:
                visited[next_point] = True
                q.append((next_point,y,weight + next_weight))


for _ in range(M):
    goal_1, goal_2 = map(int, input().split())
    print(bfs(goal_1, goal_2))

#처음에는 x == y가 아니라, x == next_point가 같으면 으로 조건문을
#잘 못 잡았다. 그래서 weight를 넣기가 애매했었다.
#x가 지금 목적지와 같으면 그대로 리턴하고, weight를 일관적으로 더해주는 방법이 맞았다. 
