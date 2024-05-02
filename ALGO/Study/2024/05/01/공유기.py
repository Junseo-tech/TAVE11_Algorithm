import sys
input = sys.stdin.readline

N,C = map(int, input().split())
routers = []
for _ in range(N):
    routers.append(int(input()))

routers.sort()

start = 1 # 공유기 끼리의 최소 거리
end = routers[-1] - routers[0] # 최대 거리

while start <= end:
    mid = (start + end) // 2
    temp = []
    temp.append(routers[0]) # 최대 거리니까 무조건 처음꺼 넣기
    for router in routers:
        if router - temp[-1] >= mid:
            temp.append(router)
    if len(temp) >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(end)


