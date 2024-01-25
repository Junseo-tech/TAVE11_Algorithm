import sys
input = sys.stdin.readline

key = input().strip()
code = input().strip()
code_key = sorted(key)

key_index = list(enumerate(key))
sorted_key_index = sorted(key_index, key=lambda x:x[1])

C = len(code)
N = len(key) # 키 길이 = 평문을 자른 마디 수
key_dict = {}

code_matrix = [[' ' for _ in range(C//N)] for _ in range(N)]

#열 먼저 돌아야 함 -> 세로로 꽂아야 하니까
for i in range(C // N): #키 길이 만큼 0 7 14 21 28 35 42 49 56 // 1 8 15x
    for j in range(N):
       code_matrix[j][i] = code[j * (C//N) + i]

for i in range(N):
    key_dict[sorted_key_index[i]] = code_matrix[i]

sorted_key_dict = dict(sorted(key_dict.items(), key=lambda x: x[0][0]))

for j in range(C//N):
    print(''.join(sorted_key_dict[k][j] for k in sorted_key_dict.keys()), end='')

print()