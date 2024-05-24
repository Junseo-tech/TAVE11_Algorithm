import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    x,y = map(int, input().split())
    board[x-1][y-1] = 1
D = int(input())
direction = deque()
for _ in range(D):
    t, d = input().strip().split()
    direction.append((int(t),d))

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]


# 1 이면 사과 있는 거
time = 0
snake = deque([(0,0)])
# 사과 없으면 몸 길이 줄여서 위치 칸 비워줘야 하니까 deque 사용해서 없애기
# 사과 있는 칸은 1임

# 처음은 오른쪽으로 이동
dir = 1
def self_touch(x,y,snake):
    for i in snake:
        if x == i[0] and y == i[1]:
            return True
    return False

while True:
    x = snake[0][0]
    y = snake[0][1]
    nx = x + dx[dir]
    ny = y + dy[dir]
    time += 1 # 몸을 늘리기 시작, 0으로 초기화 하고 시간 늘려주고 몸늘리기
    if 0<=nx<N and 0<=ny<N: # 벽에 맞아 뒤지지 않음
        if self_touch(nx,ny,snake):
            break
        if board[nx][ny] == 0: # 사과 없음
            snake.pop()
        if board[nx][ny] == 1: # 사과 있음
            board[nx][ny] = 0
        snake.appendleft((nx,ny)) # 머리

        if len(direction) != 0 and time == direction[0][0]: # 시간이 같으면 -> x초가 끝난 뒤 이동이니까 위에 이동 하고 그 다음
            t, d = direction.popleft()
            if d == 'L':
                dir = (dir + 3) % 4
            else: # 오른쪽 90도
                dir = (dir + 1) % 4
    else:
        break

print(time)
