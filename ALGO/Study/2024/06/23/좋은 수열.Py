from itertools import product
N = int(input())
numbers = [1,2,3]
candidate = []

def is_good(seq):
    pass

for pro in product(numbers, repeat=N):
    sequece = "".join(map(str, pro))
    candidate.append(sequece)

for seq in candidate:
    pass
        

