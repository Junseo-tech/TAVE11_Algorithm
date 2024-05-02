import sys
input = sys.stdin.readline
N,C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()
# 한 집에는 공유기를 하나만 설치 할 수 있고, 
    #가장 인접한 두 공유기 사이 거리를 최대한 크게 하여 설치 하려함
# 가장 인접한 두 공유기 사이의 최대 거리를 출력

# 1 2 4 8 9
start = 1
end = houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    router = []
    router.append(houses[0])
    for house in houses:
        if house - router[-1] >= mid:
            router.append(house)
    if len(router) >= C:
        start = mid + 1
    else:
        end = mid - 1

print(end)