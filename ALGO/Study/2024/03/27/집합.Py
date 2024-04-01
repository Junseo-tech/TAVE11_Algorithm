import sys
input = sys.stdin.readline
S = 0
M = int(input())

def oper(command, k):
    global S
    if command == "add":
        S = S | (1 << k)
    if command == "remove":
        S = S & ~(1 << k)
    if command == "check":
        if(S & (1 << k)):
            print(1)
        else:
            print(0)
    if command == "toggle":
        S = S ^ (1 << k)
    if command == "all":
        S = (1 << 21) - 1
    if command == "empty":
        S = 0 

for _ in range(M):
    inputs = input().split()
    if len(inputs) == 2:
        command, k = map(str, inputs)
        oper(command, int(k))
    else:
        command = inputs[0]
        oper(command, 0)    