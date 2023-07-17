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
N = int(input())
graph = [[] for _ in range(N+1)] # N+1 만큼의 공간을 만들어서 graph[N]이 N 번 정점 나타내게 (0부터 시작하니까 7이 N 가리키려면 N+1)

for _ in range(N-1): # 입력을 N-1 만큼 받음
    A , B = map(int, input().split())
    graph[A].append(B) #A번 정점에 B 넣어주고 -> graph[A] = B
    graph[B].append(A) #B번 정점에 A 넣어주고 -> graph[B] = A

#여기까지 하면 print(graph) 시에 [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

visited = [False] * (N+1)
parent = {} #딕셔너리 하나 만들어주고 여기에 {부모 : 자식} 형태로 저장 예정

def dfs(graph, v, visited = []):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(graph, i, visited)

dfs(graph, 1, visited)

parent = sorted(parent.items(), key= lambda x : x[0])

for i in range(len(parent)):
  print((str(parent[i][1])) + ' ') #리스트 0번째에서 (0,1) 중 부모 값인 1만 프린트