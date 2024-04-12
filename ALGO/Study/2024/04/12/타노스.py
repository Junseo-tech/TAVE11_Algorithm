import sys
input = sys.stdin.readline
S = list(input().strip())
zero = S.count('0') // 2
one = S.count('1') // 2

for _ in range(zero):
    S.pop(-(S[::-1].index('0'))-1) # pop 할 때 정확한 인덱스 번호를 주게 하려고 

# index는 0이 나오는 인덱스 번호가 나오는 것. 이걸 -를 취해서 뒤로 가게 해주고 -1로 해서 정확한 인덱스
# 번호를 출력하기 위함. -1 하는건 파이썬 인덱스


for _ in range(one):
    S.pop(S.index('1'))


print(''.join(S))