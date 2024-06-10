import sys
input = sys.stdin.readline

# 교실 가장 윗 칸은 (1,1) 아랫칸은 (N,N)
N = int(input())
class_room = [[0 for _ in range(N)] for _ in range(N)]
likes = {}

for _ in range(N ** 2):
    lst = list(map(int, input().split()))
    likes[lst[0]] = lst[1:]

# 인접하다 -> |r1-r2| + |c1-c2| = 1을 만족
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_like(value): # 좋아하는 학생이 인접한 칸에 가장 많은 칸, 좋아하는 학생이 많은 칸
    answer = []
    max_count = -1
    for x in range(N):
        for y in range(N):
            if class_room[x][y] == 0:
                count = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<N and 0<=ny<N:
                        if class_room[nx][ny] in value:
                            count += 1
                if count > max_count:
                    max_count = count
                    answer = [(x,y)] # answer 초기화하고 x,y 넣기
                elif count == max_count:
                    answer.append((x,y))
    return answer

def is_blank(answer): # is_like 만족이 여러개라면 인접한 칸 중 비어있는 칸이 가장 많은 칸
    max_count = -1
    new_answer = []
    for x,y in answer:
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if class_room[nx][ny] == 0:
                    count += 1
        if count > max_count:
            max_count = count
            new_answer = [(x,y)]
        elif count == max_count:
            new_answer.append((x,y))
    return new_answer

def count_like(class_room):
    score = {1 : 1, 2: 10, 3: 100, 4: 1000}
    answer = 0
    for x in range(N):
        for y in range(N):
            count = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny< N and class_room[nx][ny] in likes[class_room[x][y]]:
                    count += 1
            answer += score.get(count, 0)
            
    return answer
    

for key, value in likes.items():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    answer = []
    answer = is_like(value) # 첫번째 조건에 있는 조건에 해당하는 애들
    if len(answer) <= 1:
        class_room[answer[0][0]][answer[0][1]] = key
        continue
    else:
        new_answer = is_blank(answer)
    if len(new_answer) <= 1:
        class_room[new_answer[0][0]][new_answer[0][1]] = key
        continue
    else:
        new_answer.sort()
        class_room[new_answer[0][0]][new_answer[0][1]] = key

answer = count_like(class_room)
print(answer)