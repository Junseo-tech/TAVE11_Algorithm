import sys
input = sys.stdin.readline
# n -> 다리 건너는 트럭 수, w -> 다리의 길이, L -> 다리의 최대하중
n,w,L = map(int, input().split())
cars = list(map(int, input().split()))
bridge = [0] * w
time = 0

while bridge:
    time += 1
    bridge.pop(0)
    if cars:
        if sum(bridge) + cars[0] <= L:
            bridge.append(cars.pop(0))
        else:
            bridge.append(0)
print(time)
        
        
            