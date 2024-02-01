def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0
    for size in sizes:
        width, height = size
        if width < height:
            width, height = height, width
        max_width = max(max_width, width)
        max_height = max(max_height, height)
        answer = max_width * max_height
    return answer

sizes = [[60,50],[30,70],[60,30],[80,40]]
print(solution(sizes))