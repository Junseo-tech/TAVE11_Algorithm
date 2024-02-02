def solution(numbers):
    numbers = [str(x) for x in numbers]
    max_len = len(max(numbers, key = len))
    numbers = sorted(numbers, key = lambda x: x * max_len, reverse = True)
    answer  = ''.join(numbers)
    return str(int(answer))

numbers = [0,0,0,0]
print(solution(numbers))