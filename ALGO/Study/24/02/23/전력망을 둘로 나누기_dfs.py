def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for start, visit in wires:
        visited = [False] * (n+1)
        visited[visit] = True
        cnt = dfs(start,visited,graph)
        answer = min(abs(cnt - (n-cnt)), answer)
    return answer

def dfs(start, visited, graph):
    visited[start] = True
    count = 1 # 도는 노드 개수
    for i in graph[start]:
        if not visited[i]:
            count += dfs(i, visited, graph)
    return count

wires = [[1,2],[2,3],[3,4]]
n = 4
print(solution(n,wires))