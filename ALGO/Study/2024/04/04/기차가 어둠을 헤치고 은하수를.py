import sys
input = sys.stdin.readline
N,M = map(int, input().split())
commands = []
for _ in range(M):
    command_input = input().split()
    if len(command_input) == 3:
        command, train, seat = command_input
        commands.append((command,train,seat))
    else:
        command, train = command_input
        seat = -1
        commands.append((command, train, seat))
    
trains = [0] * N

def perform(command, train, seat):
    if command == 1:
        train = train - 1
        seat = seat -1
        trains[train]= trains[train] | (1 << seat)
    if command == 2:
        train = train - 1
        seat = seat -1
        if trains[train] & (1 << seat):
            trains[train] = trains[train] & ~(1 << seat)
    if command == 3:
        train = train - 1
        trains[train] = trains[train] << 1
        if trains[train] & (1 << 20):
            trains[train] = trains[train] & ~(1 << 20) 
    if command == 4:
        train = train - 1
        trains[train] = trains[train] >> 1

    
 
for command, train, seat in commands:
    perform(int(command), int(train), int(seat))

answer = set()
for i in trains:
        answer.add(i)

print(len(answer))
