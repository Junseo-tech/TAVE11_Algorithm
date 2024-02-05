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

def dfs(v, count):#count 값을 같이 준 이유 -> 재귀 할 때 해당 노드에 대한 count 값을 기억하려고
    count += 1 # 노드가 2이고 count 3인데 (이전 호출 스택 2,2) 4,1 4,3
    # print(count)
    print("노드 :"+  str(v) + " count " + str(count) )
    visited[v] = True
    if v == B:
        print(count)
        exit()
    for i in graph[v]:
        if not visited[i]:
            #count += 1
            #print(count)
            dfs(i, count) # i = 3 , count = 3 #(1,3) -> 최종 호출 스택 (3,3)
            # dfs(2,2)
            
    print("백트래킹 노드" + str(v) + "일 때 count" + str(count)) # 이전 호출 스택으로 돌아감
dfs(A, 0)
print(-1)