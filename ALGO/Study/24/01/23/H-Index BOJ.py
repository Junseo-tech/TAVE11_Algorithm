import sys
input = sys.stdin.readline

n = int(input())

citations = [int(i) for i in input().split()]

def solution(citations):
    answer = 0
    citations.sort(reverse = True)

    for i in range(n): 
        if all(i == 0 for i in citations):
            return 0
        if citations[i] <= answer:
            break
        answer += 1
        if i == n-1 and answer < citations[n-1]:
            return n
    return answer

print(solution(citations))

