import sys
input = sys.stdin.readline

N,M = map(int, input().split())
power = {}

for _ in range(N):
    level, number = map(str, input().split())
    power[int(number)] = level

players = [int(input()) for _ in range(M)]
players.sort()
stat = list(power.keys())   

for player in players:
    start = 0
    end = len(stat) - 1
    result = 0
    while start <= end:
        mid = (start + end) // 2 # N이 홀수 (ex.3) 이면 반올림 안된 값으로 (1)
        if stat[mid] >= player:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    print(power[stat[result]])

    