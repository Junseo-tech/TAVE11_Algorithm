# from collections import deque

# def solution(prices):
#     queue = deque(prices)
#     answer = []
#     while queue:
#         sec = 0
#         price = queue.popleft()
#         for q in queue:
#             if q >= price:
#                 sec += 1
#         answer.append(sec)
#     return answer
# -> 위 코드가 틀린 이유 ) 큰 수를 구하는게 아니라 떨어지는 순간을 구해야 함

from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    while queue:
        sec = 0
        price = queue.popleft()
        for q in queue:
            sec += 1
            if q < price:
                break
        answer.append(sec)
    return answer