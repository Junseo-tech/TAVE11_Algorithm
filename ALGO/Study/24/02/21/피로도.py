from itertools import permutations
def solution(k, dungeons):
    ans_list = []
    store = k
    for perm in permutations(dungeons, len(dungeons)):
        count = 0
        k = store
        for per in perm:
            min_cost , pay = per
            if min_cost > k:
                continue
            k = k - pay
            count += 1
        ans_list.append(count)
    answer = max(ans_list)  
    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k,dungeons))