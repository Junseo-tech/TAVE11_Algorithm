import sys
import math
input = sys.stdin.readline
N = int(input())

primeList = []

def makePrimeList(num):
    global primeList  # 함수 내에서 전역 변수를 사용하겠다고 선언합니다.
    prime = [True] * (num+1)
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            primeList.append(p)

makePrimeList(N)

start, end, temp, count = 0,0,0,0
while end < len(primeList) or temp >= N:
    if temp < N:
        temp += primeList[end]
        end += 1
    else:
        if temp == N:
            count += 1
        temp -= primeList[start]
        start += 1

print(count)
        

