import sys
from collections import deque
input = sys.stdin.readline
q = deque(list(map(int, input().strip())) for _ in range(4))
K = int(input())

def rotation(a):
    pass

for _ in range(K):
    a,b = map(int, input().split())
    if b == 1:
        q[a].rotate(1)
    if b == -1:
        q[a].rotate(-1)

