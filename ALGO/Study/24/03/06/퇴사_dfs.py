import sys
input = sys.stdin.readline
N = int(input())
graph = [[0,0]]
for _ in range(N):
    day, money = map(int, input().split())
    graph.append([day,money])
answer = 0

def dfs(day, money):
    global answer
    if day > N :
        answer = max(answer, money)
        return 
    if day + graph[day][0] <= N+1:
        dfs(day + graph[day][0], money + graph[day][1])
    dfs(day + 1, money)

dfs(1,0)
print(answer)
