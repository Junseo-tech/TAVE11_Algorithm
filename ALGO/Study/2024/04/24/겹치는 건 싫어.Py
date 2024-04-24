import sys
input = sys.stdin.readline
N, K = map(int, input().split())
sequence = list(map(int, input().split()))

start, end, max_length = 0,0,0
count_dict = {}
max_length = 0

while end < N and start <= end: 
    count_dict[sequence[end]] = count_dict.get(sequence[end], 0) + 1
    if count_dict[sequence[end]] > K:
        temp = sequence[end]
        max_length = max(max_length, (end - start))
        while count_dict[temp] > K:
            count_dict[sequence[start]] -= 1
            start += 1
    end += 1
    max_length = max(max_length, (end - start))

print(max_length)




    
