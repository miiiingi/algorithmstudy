# 전략
# 먼저 진도 100에 도달하는 경우, 그에 맞는 인덱스에 1을 저장 하고, 앞에 것이 진도가 다 되어서 pop될때, 인덱스가 1인것까지 꺼내자!
import collections 
def solution(progresses, speeds) : 
    progresses = collections.deque(progresses)
    speeds = collections.deque(speeds)

    stack = [] # 진도가 100인 작업들을 쌓을 stack    
    count = [0 for _ in range(len(progresses))]
    answer = []  # 진도가 100인 작업들의 갯수를 담을 stack
    while progresses : 
        for ind in range(len(progresses)) : 
            if progresses[ind] < 100 : 
                progresses[ind] += speeds[ind]
            if progresses[ind] >= 100 and count[ind] == 0: 
                count[ind] = 1
            elif progresses[ind] >= 100 and count[ind] == 1: 
                continue
        if progresses[0] >= 100 : 
            count_complete = 0 # need to modi
            for ind_count in range(len(progresses)) : 
                if count[ind_count] == 1 : 
                    progresses.popleft()
                    speeds.popleft()
                    count_complete += 1
            answer.append(count_complete) 
    return answer 
answer = solution([93, 30, 55], [1, 30, 5])
print(answer)