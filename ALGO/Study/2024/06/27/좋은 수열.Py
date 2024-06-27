N = int(input())

def is_good(num):
    for i in range(1, len(num)// 2 + 1):
        if num[-i:] == num[-2*i:-i]:
            return False
    return True

def makeSequence(num):
    if len(num) == N:
        print(num)
        exit()
    for i in '123':
        if is_good(num + i):
            makeSequence(num + i)

makeSequence('1')

