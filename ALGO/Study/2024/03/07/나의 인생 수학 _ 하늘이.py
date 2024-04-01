import sys

n = int(input())
graph = []
max_dp = [[-sys.maxsize] * n for _ in range(n)]
min_dp = [[sys.maxsize] * n for _ in range(n)]

for i in range(n):
    graph.append(list(input().split()))

def operation(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b

step = [(1, 0), (0, 1)]

max_dp[0][0] = int(graph[0][0])
min_dp[0][0] = int(graph[0][0])

def dfs(x, y, op):
    # 아래, 오른쪽만 방문
    for i in range(2):
        nx = x + step[i][0]
        ny = y + step[i][1]
        
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny].isdigit():
                max_dp[nx][ny] = max(operation(max_dp[x][y], int(graph[nx][ny]), op), max_dp[nx][ny])
                min_dp[nx][ny] = min(operation(min_dp[x][y], int(graph[nx][ny]), op), min_dp[nx][ny])
                dfs(nx, ny, '')
            else:
                max_dp[nx][ny] = max_dp[x][y]
                min_dp[nx][ny] = min_dp[x][y]
                dfs(nx, ny, graph[nx][ny])

dfs(0, 0, '')
print(max_dp[n-1][n-1], min_dp[n-1][n-1])