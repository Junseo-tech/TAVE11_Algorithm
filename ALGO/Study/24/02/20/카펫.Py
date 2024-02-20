def solution(brown, yellow):
    answer = []
    ans = brown + yellow
    for i in range(1, ans+1):
        if (ans % i) == 0:
            height = i
            width = ans // i
            if (width - 2) * (height - 2) == yellow:
                answer.append(width)
                answer.append(height)
                break

    return answer

brown = 8
yellow = 1
print(solution(brown, yellow)) 