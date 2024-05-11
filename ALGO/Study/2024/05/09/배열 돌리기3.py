import sys
input = sys.stdin.readline

def up_down(array): # 상하반전
    for i in range(N):
        array[i] = array[N-1-i]
    return array
def left_right(): # 좌우반전
    pass

def right(): #오른쪽으로 90
    pass

def left(): #왼쪽으로 90
    pass

def part_1(): # 5번
    pass

def part_2(): # 6번
    pass

N, M, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

for i in command:
    if i == 1:
        up_down(array)

print(array)