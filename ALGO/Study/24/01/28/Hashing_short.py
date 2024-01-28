import sys
input = sys.stdin.readline

L = int(input())
code = input().strip()

alpha = {chr(i) : i - ord('a') + 1 for i in range(ord('a'), ord('z')+1)}

count, square, r = 0,0,31

for str in code:
    count += alpha[str] * (r ** square)
    square += 1

print(count if 1 <= L <= 5 else count % 1234567891)