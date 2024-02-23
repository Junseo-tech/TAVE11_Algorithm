from collections import deque
def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for start, visit in wires:
        visited = [False] * (n+1)
        visited[visit] = True
        cnt = bfs(start, visited, graph)
        answer = min(abs(cnt - (n - cnt)), answer)
    return answer


def bfs(start, visited, graph):
    visited[start] = True
    q = deque()
    q.append(start)
    count = 1
    while q:
        start= q.popleft()
        for i in graph[start]:
            if not visited[i]:
                q.append(i)
                count += 1
                visited[i] = True
    return count

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))