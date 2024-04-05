import sys
input = sys.stdin.readline
N,X = map(int, input().split())
visit = list(map(int, input().split()))

# 기간 -> x 만큼 볼 때 최대값이 0 이 아니라면 최대값이 나오는 갯수
# 슬라이딩 윈도우 -> x 만큼 봐야 함
max_dict = {}
max_visit = 0
for i in range(X):
    max_visit += visit[i]
    max_dict[max_visit] = max_dict.get(max_visit, 0) + 1

result = max_visit
for i in range(X, N):
    max_visit -= visit[i-X]
    max_visit += visit[i]
    result = max(result, max_visit)
    if max_visit == result:
        max_dict[max_visit] = max_dict.get(result, 0) + 1
    

if result != 0:
    print(result)
    print(max_dict[result])
else:
    print("SAD")



