import sys
input = sys.stdin.readline
N,M,k = map(int, input().split())  # 학생 수, 친구 관계 수, 갖고 있는 돈 
payment = list(map(int, input().split()))
parent = [i for i in range(N+1)]

def union(a,b):
    a = find(a)
    b = find(b)
    if payment[a-1] < payment[b-1]:
        parent[b] = a
    else:
        parent[a] = b

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


for _ in range(M):
    v, w = map(int, input().split())
    union(v,w)
total = 0

new_parent = []
for i in range(1, len(parent)):
    pa = find(parent[i])
    new_parent.append(pa)

parent_set = set(new_parent)

for x in parent_set:
    total += payment[x-1]

if k >= total:
    print(total)
else:
    print("Oh no")

'''
5 3 10
1 1 1 1 1
5 4
5 3
5 2

답 : 2
'''