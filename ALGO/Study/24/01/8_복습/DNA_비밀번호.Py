import sys
input = sys.stdin.readline

S,P = map(int, input().split())
DNA = input().strip()
base_sequence = {base : 0 for base in "ACGT"}
numbers = list(map(int, input().split()))
base_sequence.update(dict(zip("ACGT",numbers)))

sub_sequence = {base : 0 for base in "ACGT"}
result = 0

for base in DNA[:P]:
    sub_sequence[base] += 1
if all(sub_sequence[base] >= base_sequence[base] for base in "ACGT"):
        result += 1

for i in range(P,S):
    sub_sequence[DNA[i-P]] -= 1
    sub_sequence[DNA[i]] += 1
    if all(sub_sequence[base] >= base_sequence[base] for base in "ACGT"):
        result += 1

print(result)