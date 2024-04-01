import sys
input = sys.stdin.readline
from collections import deque
N, K = map(int, input().split())
durability = deque(list(map(int, input().split())))
robot = deque([False] * N)
step = 0

while durability.count(0) < K:
    step += 1
    durability.rotate(1)
    robot.rotate(1)

    robot[N-1] = False

    for i in range(N-2,-1,-1):
        if robot[i] and not robot[i+1] and durability[i+1] >= 1:
            robot[i], robot[i+1] = False, True
            durability[i+1] -= 1
        
    
    robot[N-1] = False

    if durability[0] > 0:
        robot[0] = True
        durability[0] -= 1
    
print(step)