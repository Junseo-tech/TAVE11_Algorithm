def solution(numbers, target):
    global answer
    answer = 0
    def dfs(i, present):
        global answer
        if i == len(numbers):
            if present == target:
                answer += 1
            return
        dfs(i+1, present - numbers[i])
        dfs(i+1, present + numbers[i])
        return
    dfs(0,0)
    return answer