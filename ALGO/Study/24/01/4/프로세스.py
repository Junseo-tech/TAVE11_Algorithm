from collections import deque

def solution(priorities, location):
    queue = deque((idx,pro) for idx,pro in enumerate(priorities))
    answer = 0
    while queue:
        cur_process = queue.popleft()
        if any(cur_process[1] < q[1] for q in queue):
            queue.append(cur_process)
        else:
            answer += 1
            if cur_process[0] == location:
                break
    return answer

# from collections import deque 
# def solution(priorities, location):
#     answer = 0
#     pri_tupleList = []
#     for idx, prior in enumerate(priorities):
#         pri_tupleList.append((idx, prior))
    
#     tup = deque(pri_tupleList)

#     while tup: 
#         tmp = tup.popleft()
#         flag = False 
#         for t in tup:
#             if tmp[1] < t[1]:
#                 flag = True 
#                 break    
#         if flag:
#             tup.append(tmp)
            
#         else:
#             answer+=1
#             if tmp[0] == location:
#                 return answer 
                
#     return answer

# print(solution(priorities, location))