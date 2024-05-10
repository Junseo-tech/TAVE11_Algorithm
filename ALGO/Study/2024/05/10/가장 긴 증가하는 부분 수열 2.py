import sys
import bisect
input = sys.stdin.readline
N = int(input())
sequence = list(map(int, input().split()))
lis = [sequence[0]]

for i in range(1,N):
    if lis[-1] < sequence[i]:
        lis.append(sequence[i])
    else:
        idx = bisect.bisect_left(lis, sequence[i])
        lis[idx] = sequence[i]
    print(lis)
    
#print(len(lis))