import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

min_value = 1
max_value = max(lines) #802


while min_value <= max_value : # 1 6 6 같은 인풋 처럼, max랑 min이 같아야 하는 순간이 있다. 
    count = 0
    mid = (min_value + max_value) // 2
    for line in lines:
        count += line // mid
    if count >= N :
        min_value = mid + 1
    else:
        max_value = mid - 1

print(max_value) # max가 mid 값 중 최대 값이다. 최소값보다 작아지는 순간에 출력되기 때문에 정답 범위중 최댓값임.