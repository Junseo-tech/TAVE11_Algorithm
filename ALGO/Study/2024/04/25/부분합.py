'''
10 15
5 1 3 5 10 7 4 9 2 8

연속된 수 들 중에 부분합이 S

1 1
1

1

5 10
1 2 3 4 5

3

4 5
1 2 2 3

2

10 9
1 1 1 1 1 1 1 1 1 8

9

5 5
1 1 1 1 3

'''
import sys
input = sys.stdin.readline
N,S = map(int, input().split())
sequence = list(map(int, input().split()))

start, end, temp, min_length = 0, 0, 0, sys.maxsize

if sum(sequence) < S:
    print(0)
    exit()

while end < N or temp >= S:
    if temp < S and end < N :
        temp += sequence[end]
        end += 1
    else:
        min_length = min(min_length, end - start)
        temp -= sequence[start]
        start += 1
    
print(min_length)
