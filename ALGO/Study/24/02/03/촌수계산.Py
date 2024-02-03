import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
A,B = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    X,Y = map(int, input().split())
    graph[X].append(Y)
    graph[Y].append(X)

visited = [False] * (N+1)

def dfs(v, count): #count 값을 같이 준 이유 -> 재귀 할 때 해당 노드에 대한 count 값을 기억하려고
    count += 1
    print("노드 :"+  str(v) + " count " + str(count) )
    visited[v] = True
    if v == B:
        print(count-1)
        exit()
    for i in graph[v]:
        if not visited[i]:
            dfs(i, count)
dfs(A, 0)
print(-1)