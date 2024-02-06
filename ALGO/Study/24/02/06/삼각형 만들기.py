import sys
input = sys.stdin.readline

N = int(input())
triangle = []
for _ in range(N):
    triangle.append(int(input()))
triangle.sort(reverse=True)

triangle_len = sum(triangle[:3])
if N == 3:
    if triangle_len - triangle[0] <= triangle[0]:
        print(-1)
    else:
        print(sum(triangle[:3]))

else:
    if triangle_len - triangle[0] > triangle[0]:
        print(triangle_len)
        exit()
    for i in range(3,N):
        triangle_len += triangle[i] # 13 + 1 = 14
        triangle_len -= triangle[i-3] # 14 - 10 = 4
        if triangle[i-2] < triangle[i-1] + triangle[i]: # 무조건 두 변이 커야만 가능 
            print(triangle_len)
            exit()
    print(-1)

    
