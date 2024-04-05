import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))

candidate = []

for i in range(N):
    sub = sushi[i:i+k]
    if len(sub) == k:
        candidate.append(sub)
    else:
        sub = sub + sushi[:k-len(sub)]
        candidate.append(sub)

pre_answer = []
for can in candidate:
    if len(set(can)) == len(can):
        pre_answer.append(can)

if all(c in ans for ans in pre_answer):
    print(k)
else:
    print(k+1)


