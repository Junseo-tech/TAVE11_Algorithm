'''
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는
프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N이 주어진다. 둘째 줄 부터 N-1개의 줄에 트리 상에서 연결된 두 정점이
주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

입력 예시
7
1 6
6 3
3 5
4 1
2 4
4 7

출력 예시
4
6
1
3
1
4
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 
#재귀 사용해 특히 dfs, bfs 풀 때 시간 초과 뜰 때 사용한다고 함. 파이썬의 재귀 최대 깊이 기본 설정이 1000회 이하여서
#그렇다고 함 이거 때문에 한시간 걸렸네 히히 하... 암튼 최대 깊이가 바뀌어서 돌아간다고 한다. 그리고 이거 pypy는 안된다고 함.

N = int(input())

graph = [[] for _ in range(N+1)] # N+1 만큼의 공간을 만들어서 graph[N]이 N 번 정점 나타내게 (0부터 시작하니까 7이 N 가리키려면 N+1)

for _ in range(N-1): # 입력을 N-1 만큼 받음
    A , B = map(int, input().split())
    graph[A].append(B) #A번 정점에 B 넣어주고 -> graph[A] = B
    graph[B].append(A) #B번 정점에 A 넣어주고 -> graph[B] = A

#여기까지 하면 print(graph) 시에 [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

visited = [0] * (N+1) #부모

def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v #index 자리에 부모 넣기
            dfs(i)

dfs(1)

for i in range(2, N+1):
  print(visited[i])