import sys

input = sys.stdin.readline

S,P = map(int, input().split())
DNA = input().strip()
base_dict = {"A": 0 , "C": 0, "G": 0, "T": 0}

numbers = list(map(int, input().split()))

for i,key in enumerate(base_dict):
    base_dict[key] = numbers[i]

base_count = sum(base_dict.values())
result = 0

sequence_count = {"A": 0 , "C": 0, "G": 0, "T": 0}
for base in DNA[:P]:
    sequence_count[base] += 1

if all(sequence_count[base] >= base_dict[base] for base in base_dict):
    result += 1

for i in range(P,S):
    sequence_count[DNA[i-P]] -= 1
    sequence_count[DNA[i]] += 1

    if all(sequence_count[base] >= base_dict[base] for base in base_dict):
        result += 1

print(result)

