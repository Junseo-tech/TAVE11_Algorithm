import sys
input = sys.stdin.readline
H,W = map(int, input().split())
block = list(map(int, input().split()))

answer = 0
for i in range(1, len(block)-1):
    left = max(block[:i+1])
    right = max(block[i:])
    rain = min(left, right)
    answer += rain - block[i]

print(answer)




        
        




