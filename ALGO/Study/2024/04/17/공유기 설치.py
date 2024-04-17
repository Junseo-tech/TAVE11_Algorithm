import sys
input = sys.stdin.readline
N,C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()
# 한 집에는 공유기를 하나만 설치 할 수 있고, 
    #가장 인접한 두 공유기 사이 거리를 최대한 크게 하여 설치 하려함
# 가장 인접한 두 공유기 사이의 최대 거리를 출력

# 1 2 4 8 9
start = 0
end = len(house) - 1

while start <= end :
    mid = (start + end) // 2
    if house[mid] - house[start] < house[end] - house[mid] :
        pass
    else:
        pass


