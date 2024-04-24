import sys
input = sys.stdin.readline
N, K = map(int, input().split())
sequence = list(map(int, input().split()))
# K 는 겹치는 횟수 -> K = 2 이면 겹치는 숫자 개수가 2개까지 만 이어야 함. 222 4 는 안되고 22, 44는 됨
# 투 포인터
start = 0
end = 0
max_len = 0
sequence_list = []

while end < N:
    if sequence[start] != sequence[end]:
        sequence_list.append(sequence[end])
    else:
        if sequence_list.count(sequence[end]) < K:
            sequence_list.append(sequence[end])
        else: # K 보다 클 때 -> 새로운 count 
            pass
    max_len = max(max_len, len(sequence_list[:sequence[end]]))
    start = end
    end += 1


print(max_len)
    
