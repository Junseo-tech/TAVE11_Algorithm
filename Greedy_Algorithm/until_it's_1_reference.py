N, K = map(int, input().split())

result = 0

while True :
    target = (N // K) * K #이렇게 하면 나누어 떨어지는 수를 빠르게 찾음
    result += (N - target)
    N = target

    if N < K :
        break


    N //= K
    result += 1

result += (N-1)
print(result)