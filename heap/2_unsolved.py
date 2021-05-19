# 어떤 걸 기준으로 먼저 시행해야 시간이 줄어들 수 있는지 생각해보자.
# (이전작업종료시간- 다음작업시작시간) + 다음작업걸리는시간 을 비교해서 짧은 걸 먼저 처리하자.
# 1. 작업이 걸리는 시간 기준 ? 
# 2. 
import collections
def solution(jobs) : 
    jobs = sorted(jobs, key = lambda x : x[0])
    jobs = collections.deque(jobs)
    current = [] 
    current_time = 1001 
    total_time = 0 
    total_len = len(jobs)
    inter_time = 0 
    while jobs : 
        if not current : 
            current.append(jobs.popleft())
        else : 
            for ind, job in enumerate(jobs) : 
                if (current[-1][1] - job[0]) < current_time : 
                    current_time = (current[-1][1] - job[0])    
                    num_next = ind
            # jobs[num_next]인 것을 다음 작업에 처리한다.
            while True : 
                if  inter_time < current[-1][1] : 
                    inter_time += 1
                else : 
                    total_time += current.pop()[1]
                    current.append(jobs[num_next])
                    inter_time = current_time
                    del jobs[num_next]
                    break
    return total_time / total_len 
answer =solution([[0, 3], [1, 9], [2, 6]])
print(answer)