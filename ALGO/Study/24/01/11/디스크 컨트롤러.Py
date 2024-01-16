import heapq as hq

def solution(jobs):
    answer = 0
    disk_time = []
    division = len(jobs)
    pre_end = 0

    jobs.sort(key=lambda x : x[0])

    while jobs or disk_time: # 수행하지 않은 것과 대기중인 작업 모두 처리
        while jobs and jobs[0][0] <= pre_end:
            start_point, total_time = jobs.pop(0)
            hq.heappush(disk_time, (total_time, start_point)) # 걸리는 시간이 제일 작은 애로 정렬

        if disk_time:
            total_time, start_point = hq.heappop(disk_time)
            answer += pre_end + total_time - start_point
            pre_end += total_time 
        else :
            pre_end += 1 # 시간 계속 옮겨줌. 앞 선 작업이 끝나도 대기 시간을 갖고 작업해야 하는 경우 

    return answer // division

#jobs = [[1,4],[7,9], [1000,3]] 테케 19번 반례
#print(solution(jobs))
