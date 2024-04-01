import sys
input = sys.stdin.readline
N,M = map(int, input().split())
word = list(input().strip() for _ in range(N))
word_book = []
frequency = {}

for i in range(N):
    count = 0
    if len(word[i]) < M:
        continue
    frequency[word[i]] = frequency.get(word[i], 0) + 1

frequency_list = sorted(frequency.items(), key = lambda x : (- 1 * x[1], -1 * len(x[0]), x[0]))

for answer in frequency_list:
    print(answer[0])