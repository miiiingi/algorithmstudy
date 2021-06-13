# 어떤 걸 기준으로 먼저 시행해야 시간이 줄어들 수 있는지 생각해보자.
# (이전작업종료시간- 다음작업시작시간) + 다음작업걸리는시간 을 비교해서 짧은 걸 먼저 처리하자. > 이전 작업의 종료시간을 계속해서 업데이트 하는 방식
# 갯수 만큼의 리스트를 만들고, 1초가 지날 때 마다 업데이트 해주는 방식 > index의 문제가 있어서 불가능할 듯 ? >> index를 잘 설정해주는 방향으로 ..? 
# 그냥 시작시간이랑 걸리는 시간으로 계산해서 나갈까 ?? >> 그럼 종료되었다는 걸 어떻게 표현할래 ? 

import collections
import heapq
def solution(jobs) : 
    jobs = collections.deque(sorted(jobs, key = lambda x: x[0]))
    stack = False
    stack_heaq = []
    answer = 0 
    start = 0 
    while jobs : 
        if not stack : 
            current = jobs.popleft()
            start += (current[0] - start) + current[1] 
            answer += current[1]
        else : 
            pass

        
    return 
answer =solution([[1, 9], [0, 3], [2, 6]])
print(answer)