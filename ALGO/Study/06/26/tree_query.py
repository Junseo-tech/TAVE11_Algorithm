'''
간선에 가중치와 방향성이 없는 임의의 루트 있는 트리가 주어졌을 때, 아래의 쿼리에 답해보도록 하자.

정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.

입력
---
트리의 정점의 수 N과 루트의 번호 R, 쿼리의 수 Q가 주어진다. (2 ≤ N ≤ 105, 1 ≤ R ≤ N, 1 ≤ Q ≤ 105)

이어 N-1줄에 걸쳐, U V의 형태로 트리에 속한 간선의 정보가 주어진다. (1 ≤ U, V ≤ N, U ≠ V)

이는 U와 V를 양 끝점으로 하는 간선이 트리에 속함을 의미한다.

이어 Q줄에 걸쳐, 문제에 설명한 U가 하나씩 주어진다. (1 ≤ U ≤ N)

입력으로 주어지는 트리는 항상 올바른 트리임이 보장된다.

출력
---
Q줄에 걸쳐 각 쿼리의 답을 정수 하나로 출력한다.

예제 입력
---------
9 5 3
1 3
4 3
5 4
5 6
6 7
2 3
9 6
6 8
5
4
8

출력
----
9
4
1
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

N, R, Q = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    U , V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

visited = [0] * (N+1)

def countVertex(root):
    visited[root] = 1
    for i in graph[root]:
        if visited[i] == 0:
            visited[root] += countVertex(i)
    return visited[root]

countVertex(R)

for i in range(Q):
    Qu = int(input())
    print(visited[Qu])




# for _ in range(Q):
#     Qu = int(input())
#     print(dfs(graph, Qu, visited))