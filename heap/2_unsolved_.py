# 어떤 걸 기준으로 먼저 시행해야 시간이 줄어들 수 있는지 생각해보자.
# (이전작업종료시간- 다음작업시작시간) + 다음작업걸리는시간 을 비교해서 짧은 걸 먼저 처리하자.
# 갯수 만큼의 리스트를 만들고, 1초가 지날 때 마다 업데이트 해주는 방식 > index의 문제가 있어서 불가능할 듯 ? >> index를 잘 설정해주는 방향으로 ..? 
# 그냥 시작시간이랑 걸리는 시간으로 계산해서 나갈까 ?? >> 그럼 종료되었다는 걸 어떻게 표현할래 ? 

import collections
def solution(jobs) : 
    list_implementing = [] 
    list_time = [1 for _ in range(len(jobs))] 
    jobs = sorted(jobs, key = lambda x : x[0])
    jobs = collections.deque(jobs)
    time_total = 0 
    while jobs : 
        if not list_implementing : 
            index_current = jobs[0][0]
            list_implementing.append(jobs.popleft())
        else : 
            if list_time[index_current] == list_implementing[0][1] :  
                list_implementing.pop()



    return 
answer =solution([[0, 3], [1, 9], [2, 6]])
print(answer)