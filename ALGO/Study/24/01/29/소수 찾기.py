from itertools import permutations

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    number = []
    answer = 0
    number_set = set()
    for i in numbers:
        number.append(int(i))
    
    for i in range(1, len(number)+1):
        for per in permutations(number,i):
            num = int(''.join(map(str,per))) #튜플 나오는거 다시 숫자로
            number_set.add(num)
        
    for n in number_set:
        print(n)
        if isPrime(n):
            answer += 1
    return answer

numbers = "011"
print(solution(numbers))
