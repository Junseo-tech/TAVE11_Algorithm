import sys
input = sys.stdin.readline
R, C, T = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

up, down = -1, -1

for i in range(R):
    if area[i][0] == -1:
        up = i
        down = i + 1
        break

def diffusion():
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if area[i][j] > 0:
                count = 0
                amount = area[i][j] // 5
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and area[nx][ny] != -1:
                        temp[nx][ny] += amount
                        count += 1
                temp[i][j] += area[i][j] - amount * count
            elif area[i][j] == -1:
                temp[i][j] = -1

    for i in range(R):
        for j in range(C):
            area[i][j] = temp[i][j]

def air_fresh_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    before = 0
    direction = 0
    x, y = up, 1
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direction += 1
            continue
        area[x][y], before = before, area[x][y]
        x = nx
        y = ny

def air_fresh_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    before = 0
    direction = 0
    x, y = down, 1
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direction += 1
            continue
        area[x][y], before = before, area[x][y]
        x = nx
        y = ny

for _ in range(T):
    diffusion()
    air_fresh_up()
    air_fresh_down()

answer = 0
for i in range(R):
    for j in range(C):
        if area[i][j] > 0:
            answer += area[i][j]

print(answer)
