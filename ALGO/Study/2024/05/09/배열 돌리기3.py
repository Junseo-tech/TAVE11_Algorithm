import sys
input = sys.stdin.readline


def up_down(array): # 상하반전
    N = len(array)
    M = len(array[0])
    arr = [[0] * M for _ in range(N)]
    for i in range(N):
        arr[i] = array[N-1-i]
    return arr

def left_right(array): # 좌우반전
    N = len(array)
    M = len(array[0])
    arr = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            arr[i][j] = array[i][M-1-j]
    return arr

def right(array): #오른쪽으로 90
    N = len(array)
    M = len(array[0])
    arr = [[0] * N for _ in range(M)]
    for j in range(M):
        for i in range(N):
            arr[j][N-i-1] = array[i][j]
    return arr
    
def left(array): #왼쪽으로 90
    N = len(array)
    M = len(array[0])
    arr = [[0] * N for _ in range(M)]
    for j in range(M-1,-1,-1):
        for i in range(N):
            arr[M-j-1][i] = array[i][j]
    return arr

def part_1(array): # 5번
    N = len(array)
    M = len(array[0])
    arr = [[0] * M for _ in range(N)]
    for i in range(N//2): # N = 6, M = 8
        for j in range(M//2):
            arr[i][j + M//2] = array[i][j]
            arr[i + N//2][j+M//2] = array[i][j+M//2]
            arr[i + N//2][j] = array[i + N//2][j+M//2]
            arr[i][j] = array[i+N//2][j]
    return arr


def part_2(array): # 6번
    N = len(array)
    M = len(array[0])
    arr = [[0] * M for _ in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            arr[i][j] = array[i][j+M//2]
            arr[i][j+M//2] = array[i+N//2][j+M//2]
            arr[i+N//2][j+M//2] = array[i+N//2][j]
            arr[i+N//2][j] = array[i][j]
    return arr

N, M, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

for i in command:
    if i == 1:
        array = up_down(array)
    if i == 2:
        array = left_right(array)
    if i == 3:
        array = right(array)
    if i == 4:
        array = left(array)
    if i == 5:
        array = part_1(array)
    if i == 6:
        array = part_2(array)

for arr in array:
    print(*arr)