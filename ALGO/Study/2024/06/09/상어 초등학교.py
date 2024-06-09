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

def is_like(): # 좋아하는 학생이 인접한 칸에 가장 많은 칸
    pass

def is_blank(): # is_like 만족이 여러개라면 인접한 칸 중 비어있는 칸이 가장 많은 칸
    pass


