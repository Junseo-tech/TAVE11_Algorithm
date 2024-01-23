def solution(citations):
    answer = 0
    n = len(citations)
    
    citations.sort(reverse = True) #[6,5,3,1,0] -> 인용 횟수
    
    for i in range(n): 
        if all(i == 0 for i in citations):
            return 0
        if citations[i] <= answer:
            break
        answer += 1
        if i == n-1 and answer < citations[n-1]:
            return n
    return answer

citations = [9,10,11]
print(solution(citations))