import sys
input = sys.stdin.readline

p,m = map(int, input().split())
players = []
for _ in range(p):
    level, name = map(str, input().strip().split())
    players.append([int(level), name])


waits = []
for player in players:
    is_matched = False
    for wait in waits:
        if len(wait) < m and wait[0][0]-10 <= player[0] <= wait[0][0]+10:
            wait.append(player)
            is_matched = True
            break
    if not is_matched:
        waits.append([[player[0], player[1]]])

for wait in waits:
    if len(wait) == m:
        print("Started!")
    else:
        print("Waiting!")
    wait.sort(key = lambda x : x[1])

    for i in wait:
        print(' '.join(map(str, i)))
