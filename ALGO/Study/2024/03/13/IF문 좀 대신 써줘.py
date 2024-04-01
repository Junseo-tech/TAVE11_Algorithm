import sys
input = sys.stdin.readline
N,M = map(int, input().split())
power_list = []
for _ in range(N):
    power, level = map(str, input().split())
    power_list.append((power, level))

power_list.sort(key = lambda x : int(x[1]))
players = list(int(input()) for _ in range(M))

for player in players:
    start = 0
    end = len(power_list) - 1
    result = 0
    while start <= end:
        mid = (start+end) // 2
        if int(power_list[mid][1]) >= player:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    print(power_list[result][0])




    