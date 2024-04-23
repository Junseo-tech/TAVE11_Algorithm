import math

max_weight = int(math.sqrt(100000))
G = int(input()) # 현재 몸무게의 제곱에서 기억하고 있던 몸무게 뺀 거

# 현재 몸무게로 가능한 것을 모두 출력
weight = []
for i in range(1, int(G ** 0.5) + 1):
    if G % i == 0:
        B = G // i
        if i > B:
            break
        for a in range(1, G + 1):
            b = B - a
            if (a + b) == B and (a-b) == i:
                if a > 0 and isinstance(a , int) and b > 0 and isinstance(b, int) and a != b:
                    if a < b:
                        weight.append(b)
                    weight.append(a)
                else:
                    continue


weight.sort()
for i in range(len(weight)):
    print(weight[i])

if len(weight) == 0:
    print(-1)



