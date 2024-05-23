import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

# 먹을 물고기 공간에 없으면 엄마한테 헬프
# 먹을 수 있는 물고기 1, 걔 먹음
# 먹을 수 있는 물고기 1보다 많으면 가장 가까운 애 -> 칸 개수의 최소값
# 거리 가까운 애 많으면 가장 위에 , 가장 위도 같으면 가장 왼쪽
# 이동과 동시에 물고기 냠냠 + 물고기 먹으면 빈 칸
# 크기 작은 물고기만 섭취 가능, 같으면 먹을 수 없지만 패스 쌉가능
# 지 크기만큼 먹으면 크기 1 증가
# 엄마 부르는데 얼마나 걸리는지 구하기
# 0 : 빈칸, 칸에 있는 물고기 크기 (10보다 작음) , 9 아가 위치 -> 한마리

shark_dir = deque()
fish = deque()
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark_dir.append((i,j))
            space[i][j] = 0
        if space[i][j] > 0 and space[i][j] < 7:
            fish.append((i,j))

# 먹을 수 있는 애들 한테 가는 중에 더 큰 애들 있으면 지나가지 못하는 거 유의하기

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(shark_x, shark_y, shark):
    q = deque([(shark_x, shark_y)])
    visited = [[False] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    visited[shark_x][shark_y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and shark >= space[nx][ny]:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny))
                visited[nx][ny] = True
    return distance

shark = 2
time = 0
fish_count = 0

while True:
    if fish_count == shark:
        shark += 1
        fish_count = 0

    min_distance = float('inf')
    shark_x, shark_y = shark_dir[0]
    distance = bfs(shark_x, shark_y, shark)
    candidate = []
    for x,y in fish:
        if distance[x][y] != 0 and space[x][y] < shark: # 먹을 수 있는 애들 다 담기
            if min_distance > distance[x][y]:
                min_distance = distance[x][y]
                candidate = [(x,y)]
            if min_distance == distance[x][y]:
                candidate.append((x,y))

    if len(candidate) == 0:
        break
    candidate.sort()
    min_x, min_y = candidate[0] # 잡아 먹을 애
    space[min_x][min_y] = 0 # 먹힘
    fish_count += 1 # 먹혔다 처리

    fish.remove((min_x, min_y))

    time += min_distance

    shark_dir.pop()
    shark_dir.append((min_x, min_y))

print(time)


        

    

