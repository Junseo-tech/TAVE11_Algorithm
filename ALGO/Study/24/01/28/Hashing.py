import sys
input = sys.stdin.readline

L = int(input())
hash = input().strip()

# alpha = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,
#  'k':11, 'l' : 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
#  's': 19, 't': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y':25,'z': 26}

alpha = {chr(i) : i - ord('a') + 1 for i in range(ord('a'), ord('z')+1)}

# r = 31
# count = 0
# square = 0
count,r,square = 31,0,0
for str in hash:
    multiply_num = int(alpha[str])
    count += multiply_num * (r ** square)
    square += 1

# if 1 <= L <= 5:
#     print(count)
# else:
#     print(count % 1234567891)

print(count if 1 <= L <= 5 else count % 1234567891)