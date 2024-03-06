import sys
input = sys.stdin.readline
N,D = map(int, input().split())
load = [list(map(int, input().split())) for _ in range(N)] + [[0,0,0]]
load.sort()
dp = [i for i in range(D+1)]
visit = set()
for i in range(N+1):
    start, destination, shortest = load[i]
    if destination > D:
        continue
    if destination - start < shortest:
        continue

    visit.add(start)
    visit.add(destination)

    for place in visit:
        if start > place:
            dp[start] = min(dp[start], dp[place] + start - place)
    dp[destination] = min(dp[destination], dp[start] + shortest)
    dp[D] = min(dp[D], dp[destination] + D - destination)

print(dp[D])

