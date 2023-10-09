import sys

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
dic = dict()
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] in dic:
            dic[arr[i][j]] += (10**(len(arr[i])-j))
        else:
            dic[arr[i][j]] = (10**(len(arr[i]) - j))
dic = sorted(dic.items(), key=lambda x: -x[1])

newdic = dict()

i = 0
for key, value in dic:
    newdic[key] = 9-i
    i += 1

answer = []
for i in range(len(arr)):
    n = 0
    for s in arr[i]:
        n += newdic[s]
        n *= 10
    n //= 10
    answer.append(n)
print(sum(answer))