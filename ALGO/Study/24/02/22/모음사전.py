from itertools import product
def solution(word):
    answer = words.index(word)
    return answer

alpabet = ["A","E","I","O","U"]
words = []
for i in range(1,6):
    for per in product(alpabet, repeat = i):
        alp = ''.join(map(str,per))
        words.append(alp)
        words.sort()

word = "AAAAE"
print(solution(word) + 1)

    

