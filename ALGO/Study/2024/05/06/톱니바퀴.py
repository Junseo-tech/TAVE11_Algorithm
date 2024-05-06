import sys
from collections import deque
input = sys.stdin.readline
system = []
for _ in range(4):
    temp = deque(list(map(int, input().strip())))
    system.append(temp)
K = int(input())

def is_turn_left(number,l):
    if number < 0:
        return False
    if system[number][2] != l:
        return True

def is_turn_right(number,r):
    if number > 3:
        return False
    if system[number][6] != r:
        return True

def turn(direction, number):
    if direction == -1:
        system[number].rotate(-1)
    if direction == 1:
        system[number].rotate(1)

def move_system(number, direction):
    if number > 3 and number < 0:
        return
    visited[number] = True
    l , r = system[number][6], system[number][2]
    turn(direction, number)
    if is_turn_left(number-1, l) and not visited[number-1]:
        move_system(number-1, -direction)
    if is_turn_right(number + 1, r) and not visited[number+1]:
        move_system(number+1, -direction)

for _ in range(K):
    a, b = map(int, input().split())
    visited = [False for _ in range(4)]
    move_system(a-1, b)

answer = 0
if system[0][0] == 1:
    answer += 1
if system[1][0] == 1:
    answer += 2
if system[2][0] == 1:
    answer += 4
if system[3][0] == 1:
    answer += 8

print(answer)

