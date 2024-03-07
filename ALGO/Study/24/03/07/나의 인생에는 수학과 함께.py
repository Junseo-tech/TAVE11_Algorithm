import sys
input = sys.stdin.readline
N = int(input())
load = []

for _ in range(N):
    load.append(list(map(str, input().rstrip().split())))

## eval 쓰기 -> 문자열로 표현되는 표현식 실행해서 결과값을 받아옴
# operators = ['+', '*', '-']
# for i in range(N):
#     for j in range(len(load[i])):
#         if load[i][j] not in operators:
#             load[i][j] = int(load[i][j])

min_ans = (10 ** 10)
max_ans = -(10 ** 10)

def dfs(x, y, present):
    global min_ans
    global max_ans
    if x == N-1 and y == N-1:
        min_ans = min(min_ans, int(eval(present)))
        max_ans = max(max_ans, int(eval(present)))
        return 
    if (x+y) % 2 == 0:
        if x+1 < N:
            dfs(x+1, y, present + load[x+1][y])
        if y+1 < N:
            dfs(x,y+1, present + load[x][y+1])
    else:
        if x+1 < N:
            dfs(x+1, y, str(eval(present + load[x+1][y])))
        if y+1 < N :
            dfs(x, y+1, str(eval(present + load[x][y+1])))

dfs(0,0,load[0][0])
print(max_ans, min_ans)



    


    

    





