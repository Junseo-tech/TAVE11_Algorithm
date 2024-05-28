import sys
input = sys.stdin.readline
from collections import deque

bryan = input().strip()
ans = ""
temp = deque()

# P P P A P A P
for i in range(len(bryan)): # 1,000,000 
    if len(temp) == 4:
        if list(temp) == ['P','P','A','P']:
            ans += "P"
            temp.clear()
        else:
            ans += temp.popleft()
    if len(temp) < 4:
        temp.append(bryan[i])

if len(temp) > 0:
    while len(temp) != 0:
        ans += temp.popleft()

if ans == "PPAP":
    print("PPAP")
else:
    print("NP")