# 전략
# 일단 적혀있는 알고리즘을 그대로 구현해보자.
# 1. 문제를 구현
# 2. location에 해당하는 정답을 도출하는 구현
# 3. 최적화
import collections
def solution(priorities, location) : 
    for ind, x in enumerate(priorities) : 
        priorities[ind] = (ind, x)
    priorities = collections.deque(priorities)
    answers = [] 
    while True : 
        max_base = priorities.popleft()
        if priorities : 
            if max_base[1] < max(priorities, key = lambda x : x[1])[1] : 
                priorities.append(max_base)
            else : 
                answers.append(max_base)
        else : 
            answers.append(max_base)
            break
    for ind2, answer in enumerate(answers) : 
        if answer[0] == location : 
            return ind2+1
answer = solution([2,1,3,2],2)
# answer2 = solution([1,1,9,1,1,1],0)
print(answer)