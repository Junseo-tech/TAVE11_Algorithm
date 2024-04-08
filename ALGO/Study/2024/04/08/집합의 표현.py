import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n,m = map(int, input().split())
calculation = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]

def set_calculate(oper, a, b):
    answer = set ()
    if oper == 0:
        union(a,b)
    if oper == 1:
        a = find(a)
        answer.add(a)
        b = find(b)
        answer.add(b)
        if len(answer) == 1:
            print("YES")
        else:
            print("NO")


def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(m):
    for j in range(3):
        oper = calculation[i][0]
        a = calculation[i][1]
        b = calculation[i][2]
    set_calculate(oper,a,b)