import sys
input = sys.stdin.readline
N, K = map(int, input().split())
sequence = list(map(int, input().split()))
count = [0] * (max(sequence) + 1)
left, right = 0,0
answer = 0

while right < N:
    if count[sequence[right]] < K:
        count[sequence[right]] += 1
        right += 1
    else:
        count[sequence[left]] -= 1
        left += 1
    answer = max(answer, right-left)

print(answer)