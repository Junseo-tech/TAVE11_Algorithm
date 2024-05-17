import sys
input = sys.stdin.readline
from functools import cmp_to_key
N = int(input())
calendar = []
for _ in range(N):
    S, E = map(int, input().split())
    calendar.append((S,E))

# 시작 날이 같은 경우 기간이 긴 것이 앞으로 오게 정렬
calendar.sort(key = cmp_to_key(lambda x,y: -1 if x[0]==y[0] and (x[1] - x[0] > y[1] - y[0]) else 1))

max_end = calendar[0][1]
height = 0
min_start = calendar[0][0]
answer = []
R = calendar[N-1][1]
is_upper = [0 for _ in range(366)]

for i in range(calendar[0][0], calendar[0][1]):
    is_upper[i] = 1

for i in range(1, N):
    if max_end >= calendar[i][0] or calendar[i-1][1] + 1 == calendar[i][0]: # 앞의 것 중 가장 큰 end가 끝이 뒤의 시작 보다 크거나 같을 때 -> 포함
        if calendar[i-1][1] < calendar[i][0] and is_upper[calendar[i][0]] == 0: # 앞의 것의 시작이 뒤의 것의 시작보다 작을 때 -> 위에 쌓기
            # 높이 변화 없음, 넓이만
            for j in range(calendar[i][0], calendar[i][1] + 1):
                is_upper[j] = 1
                print(is_upper)
        if calendar[i-1][1] >= calendar[i][0] and is_upper[calendar[i][0]] == 1: # 높이 변화 있어야 함 
            height += 1
    else: # 포함 안될 때
        answer.append((min_start, max_end, height))
        min_start = calendar[i][0]
        max_end = calendar[i][1]
        height = 1
        continue
    max_end = max(max_end, calendar[i][1])

if len(answer) == 0:
    answer.append((min_start, max_end, height)) 

print(answer)
print(calendar)
    
