def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]

    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    for start, visit in wires:
        visited = [False] * (n+1)

        visited[visit] = True # 연결 끊어버림
        cnt = dfs(graph,start,visited)
        answer = min(abs(cnt-(n-cnt)),answer)
    return answer

def dfs(graph, start, visited):
    count = 1
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            count += dfs(graph,i,visited) # start 와 연결되어 있는 모든 노드의 결과 값을 알아야 함
    return count

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n,wires))