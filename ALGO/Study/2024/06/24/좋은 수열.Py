from itertools import product
N = int(input())
numbers = [1,2,3]
candidate = []

def is_good(seq):
    for i in range(1,len(seq)//2 + 1): # 123123
        for j in range(len(seq)-2*i+1): # i == 1
            if seq[j:j+i] == seq[j+i:j+2*i]:
                return False
    return True

for pro in product(numbers, repeat=N):
    sequece = "".join(map(str, pro))
    candidate.append(sequece)

answer = []
for seq in candidate:
    if is_good(seq):
        answer.append(seq)

answer.sort()
print(answer[0])
        

