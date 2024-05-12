import sys
input = sys.stdin.readline
N,K = map(int, input().split())

def isPrime(num, K):
    prime = [True] * (num + 1)
    p = 2
    count = 0
    while p <= num:
        if prime[p]:
            for i in range(p , num+1, p):
                if prime[i]:
                    prime[i] = False
                    count += 1
                if count == K:
                    return i
        p += 1

print(isPrime(N, K))