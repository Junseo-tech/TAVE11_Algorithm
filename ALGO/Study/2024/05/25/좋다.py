import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

answer = 0
for i in range(N):
    start, end = 0, N-1
    while start < end and end < N:
        # 자기 자신과 더해지면 안된다
        if i == start:
            start += 1
            continue
        if i == end:
            end -= 1
            continue
        if numbers[start] + numbers[end] == numbers[i]:
            answer += 1
            break
        if numbers[start] + numbers[end] < numbers[i]:
            start += 1
        if numbers[start] + numbers[end] > numbers[i]:
            end -= 1
    
print(answer)

# 자기 자신과 더해지면 안되는데에 해당하는 반례
'''
5
0 0 0 0 1
답 : 4
'''