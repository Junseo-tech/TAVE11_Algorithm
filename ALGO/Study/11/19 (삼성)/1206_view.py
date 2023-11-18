import sys
sys.stdin = open("input.txt", "r")


for test in range(10):
    result = 0
    N = int(input())
    building = list(map(int, input().split()))

    for i in range(2, N-2):
        left_max = max(building[i-1], building[i-2])
        right_max = max(building[i+1], building[i+2])
        max_height = max(left_max, right_max)
        if building[i] > max_height:
            minus = building[i] - max_height
            result += minus

    print(f"#{test} {result}")