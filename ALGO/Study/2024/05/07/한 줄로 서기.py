import sys
input = sys.stdin.readline
N = int(input())
line = list(map(int, input().split()))
answer = [0 for _ in range(N)]

# answer가 일단 자리가 비어있어야 채울 수 있음
# 자릿수 만큼 자리를 띄워서 저장한다

for i in range(N):
    count = 0 # 앞에 자기보다 큰 애가 몇 개 있는지 세는 거
    for j in range(N):
        if line[i] == count and answer[j] == 0:
            answer[j] = i + 1
            break
        if answer[j] == 0: # answer[j] 가 0 이라는건 자기랑 같은게 없다는 것
            count += 1
        # answer[j]가 0이 아니면 앞에 자기랑 같은 애가 있다는 거니까 count 높이면 안됨
    
print(*answer)