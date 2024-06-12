import sys
input = sys.stdin.readline

N,M,x,y,K = map(int, input().split())
# N : 세로, M : 가로, x,y : 좌표, K : 명령의 개수
maps = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

dice = [0] * 6 # 주사위 초기화
# [왼, 바닥, 오, 위, 아래, 뚜껑]

current_x , current_y = x, y
# 동 서 남 북
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def move(num, current_x, current_y, dice): # 4면만 변한다
    # 지도 바깥으로 이동시 false 출력
    nx = current_x + dx[num-1]
    ny = current_y + dy[num-1]
    if 0 > nx or nx >= N or ny < 0 or ny >= M:
        return False, current_x, current_y, dice

    if num == 1: #동쪽 -> 옆면 중 위, 아 안바뀜
        dice[0], dice[1], dice[2], dice[5] = dice[1], dice[2], dice[5], dice[0]
    elif num == 2: #서쪽
        dice[0], dice[1], dice[2], dice[5] = dice[5], dice[0], dice[1], dice[2]
    elif num == 3: #북쪽
        dice[1], dice[3], dice[4], dice[5] = dice[3], dice[5], dice[1], dice[4]
    elif num == 4: #남쪽
        dice[1], dice[3], dice[4], dice[5] = dice[4], dice[1], dice[5], dice[3]
    
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[1]
    else:
        dice[1] = maps[nx][ny]
        maps[nx][ny] = 0
    
    return True, nx, ny, dice

# 윗 면에 쓰여 있는 수를 출력 
for order in orders: 
    flag, x, y, dice = move(order , current_x, current_y, dice) # 지도 바깥으로 이동하면 False 출력할것
    #print("dice", count , dice, "order", order, "x", x, "y", y)
    current_x, current_y = x,y
    if flag:
        print(dice[5])