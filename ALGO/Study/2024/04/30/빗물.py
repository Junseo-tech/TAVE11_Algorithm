import sys
input = sys.stdin.readline
H,W = map(int, input().split())
block = list(map(int, input().split()))

max_block = block[0]
start, end, rain, temp = 0,0,0,0

while end < W:
    end += 1
    if end < W and block[start] <= block[end]: # start 보다 더 큰 것이 있을 때
        temp = block[start]
        print("start", block[start])
        for i in range(end):
            rain += temp - block[i]
    else:
        pass
    start = end + 1
    temp = 0

print(rain)
        




