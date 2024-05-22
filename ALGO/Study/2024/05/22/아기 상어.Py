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
        if space[i][j] > 0 and space[i][j] < 7:
            fish.append((i,j))

shark = 2
time = 0
fish_count = 0
while True:
    min_dis = 50
    if len(fish) == 0:
        break
    if len(fish) == 1:
        x,y = fish.pop()
        if space[x][y] < shark:
            time += abs(shark_dir[0][0] - x) + abs(shark_dir[0][1] - y) 
        break
    if len(fish) > 1:
        for x,y in fish:
            if min_dis > abs(shark_dir[0][0] - x) + abs(shark_dir[0][1] - y) and space[x][y] < shark:
                min_x = x
                min_y = y
                min_dis = abs(shark_dir[0][0] - x) + abs(shark_dir[0][1] - y)
            if min_dis == abs(shark_dir[0][0] - x) + abs(shark_dir[0][1] - y): # 같을 경우
                if min_x > x:
                    min_x = x
                    min_y = y
                if min_x == x:
                    if min_y > y:
                        min_x = x
                        min_y = y
        time += min_dis
        fish.remove((min_x, min_y))
        fish_count += 1
        if shark == fish_count:
            shark += 1
        space[min_x][min_y] = 0
        shark_dir.pop()
        shark_dir.append((min_x, min_y))
        
print(time)