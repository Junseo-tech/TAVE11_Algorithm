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