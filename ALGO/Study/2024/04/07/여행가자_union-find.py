import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
linked_city = [list(map(int, input().split())) for _ in range(N)]
route = list(map(int, input().split()))

parent_set = set()
parent = [i for i in range(N+1)]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(N):
    for j in range(N):
        if linked_city[i][j] == 1:
            union(i+1, j+1)

for city in route:
    parent_set.add(parent[city])
    if len(parent_set) > 1:
        print("NO")
        exit()

print("YES")

    
