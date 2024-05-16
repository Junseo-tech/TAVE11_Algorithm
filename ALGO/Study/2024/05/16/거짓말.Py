import sys
input = sys.stdin.readline
N,M = map(int, input().split())
know = list(map(int, input().split())) # 첫 번째 수는 사람 수 -> 알고 있는 사람 
parties = [list(map(int, input().split())) for _ in range(M)]
parent = [i for i in range(N+1)]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for party in parties:
    if len(party) == 2:
        continue
    for p in range(1, len(party)-1):
        union(party[p], party[p+1])

new_know = []
for k in range(1,len(know)):
    pa = find(know[k])
    new_know.append(pa)

answer = 0
for party in parties:
    P = len(party)-1
    count = 0
    for i in range(1, P+1):
        if find(parent[party[i]]) not in new_know:
            count += 1
    if count == P:
        answer += 1

print(answer)