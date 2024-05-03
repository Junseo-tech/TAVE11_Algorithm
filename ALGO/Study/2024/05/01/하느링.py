# 다이어트

# 현재^2 - 기억^2 = G
# (현재 - 기억) * (현재 + 기억) = G
# (현재 + 기억) <= G

g = int(input())
recent = 1
remember = 1
p = 1

while recent + remember <= g:
    num = recent ** 2 - remember ** 2
    if num > g:
        remember += 1
    else:
        if num == g:
            print(recent)
            p = 0
        recent += 1

if p:
    print(-1)