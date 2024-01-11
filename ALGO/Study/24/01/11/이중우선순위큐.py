import heapq as hq

def solution(operations):
    answer = []
    for operation in operations :
        oper = operation.split()
        
        if oper[0] == "I":
            hq.heappush(answer, int(oper[1]))
        if oper[0] == "D" and int(oper[1]) == -1:
            if answer:
                hq.heappop(answer)
        if oper[0] == "D" and int(oper[1]) == 1:
            if answer:
                answer.remove(max(answer))
                hq.heapify(answer)
                            
    return [max(answer), min(answer)] if answer else [0,0]