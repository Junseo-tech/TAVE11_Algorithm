from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = bfs(begin,target,words)
    return answer

def bfs(word, target, words):
    q = deque()
    q.append((word, 0))
    check = set()
    while q:
        current, count = q.popleft()
        if current == target:
            return count
        check.add(current)
        for word in words:
            if word not in check and isDifferent(current,word)==1:
                q.append((word,count+1))
    return count

def isDifferent(begin,word):
    count = 0
    for i in range(len(begin)):
        if begin[i] != word[i]:
            count += 1
    return count


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
#solution(begin,target,words)
print(solution(begin,target,words))