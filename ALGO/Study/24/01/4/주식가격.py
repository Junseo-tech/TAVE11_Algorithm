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

# def solution(prices):
#     lst = []
#     for i in range(len(prices)) :
#         cnt = 0
#         for j in range(i+1, len(prices)) : # prices[0]과 [1, 2, 3, 4] 비교해보기 
#             if prices[i] <= prices[j] : # 떨어지지 않으면 카운트 +1
#                 cnt += 1
#             else : # 떨어지면 카운트 후에 반복문 나가기 
#                 cnt += 1
#                 break
#         lst.append(cnt)
#     return lst