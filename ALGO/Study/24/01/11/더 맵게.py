import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) <= 1 :
            return -1
        answer += 1 # 맨 처음 연산도 +1 이니까
        
        first = heapq.heappop(scoville) # 제일 작은 값
        if first >= K:
            break 
            
        second = heapq.heappop(scoville) # 두 번째
        heapq.heappush(scoville,first + second*2)
        
    return answer