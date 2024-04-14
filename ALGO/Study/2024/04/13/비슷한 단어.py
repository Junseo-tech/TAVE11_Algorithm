import sys
from itertools import product
input = sys.stdin.readline

# 같은 종류의 문자로 이루어져 있고, 같은 문자는 같은 개수 만큼 있다 -> 같은 구성을 갖는다
# 두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나 빼거나 하나의 문자를 다른 문자로 바꾸어
# 나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들 두 단어를 서로 비슷한 단어라고 한다. 
# ex) DOG 와 GOD는 같은 구성을 가져서 비슷한단어 
# ex) GOD에서 O 하나 추가 되면 GOOD 이어서 비슷한 단어
# ex) DOG 에서 하나의 문자를 더하거나 빼거나 바꾸어도 DOLL은 안되어서 둘은 비슷한 단어 아님

N = int(input())
target = input().strip()
target_dict = {}

for t in target:
    target_dict[t] = target_dict.get(t, 0) + 1

words = [list(map(str, input().strip())) for _ in range(N-1)]

count = len(words)

# D DDD 이면 0 
for i in range(N-1):
    check = {}
    for j in range(len(words[i])):
        check[words[i][j]] = check.get(words[i][j], 0) + 1
        if check[words[i][j]] > 1 :
            count -= 1
            break

print(count)