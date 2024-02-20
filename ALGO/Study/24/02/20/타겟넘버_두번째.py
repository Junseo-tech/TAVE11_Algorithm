from itertools import product
def solution(numbers,target):
    l = [(-x,x) for x in numbers]
    ans = list(map(sum,product(*l)))
    return ans.count(target)