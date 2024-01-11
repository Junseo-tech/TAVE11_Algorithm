import heapq as hq
jobs = [[0, 3], [1, 9], [2, 6]]

def solution(jobs):
    answer = 0
    disk_time = [] 
    # 이전 것의 총 걸린 시간 + 내 것의 걸리는 시간(이걸 최소로 하는 heap을 만들어서 뺄까?
    # 이전 것의 총 걸린 시간 + 내 것의 걸린 시간 - 내가 들어온 시간
    # pre의 end 포인트 + 나의 소요시간 - 나의 시작 포인트 -> 전게 저장 되어야 함
    division = len(jobs) # 3
    answer = 0
    pre_end = 0
    for job in jobs:
        hq.heappush(disk_time, (job[1] - job[0],job[0], job[1])) # 걸리는 시간, 시점, 소요시간
        # 걸리는 시간 기준으로 minheap
    while disk_time:
        run_time, start_point,total_time = hq.heappop(disk_time)
        pre_end = start_point + total_time  #pre_end가 누적 되면 안됨
        answer += pre_end
        print(pre_end)

    return answer

print(solution(jobs))