# 전략
# 먼저 진도 100에 도달하는 경우, 그에 맞는 인덱스에 1을 저장 하고, 앞에 것이 진도가 다 되어서 pop될때, 인덱스가 1인것까지 꺼내자! 
# 중요한 것은 앞에 것이 0인 경우 뒤에 것이 0이더라도 꺼내지 않는 다는 것
import collections 
def solution(progresses, speeds) : 
    progresses = collections.deque(progresses)
    speeds = collections.deque(speeds)
    count = collections.deque([0 for _ in range(len(progresses))])

    answer = [] # 한 번에 완료되는 작업들의 갯수를 담을 리스트
    while progresses : 
        for ind in range(len(progresses)) : 
            if progresses[ind] < 100 : 
                progresses[ind] += speeds[ind]
            if progresses[ind] >= 100 and count[ind] == 0: 
                count[ind] = 1
            elif progresses[ind] >= 100 and count[ind] == 1: 
                continue
        if progresses[0] >= 100 : 
            stack = [] # 처음 작업이 완료 되었을 때, 얼마나 많은 작업이 담길 수 있는지를 나타내는 리스트
            progresses.popleft()
            speeds.popleft()
            stack.append(count.popleft())
            try : 
                while stack and progresses[0] >= 100 : 
                    progresses.popleft()
                    speeds.popleft()
                    stack.append(count.popleft())
            except : 
                pass
            answer.append(len(stack)) 
    return answer 
answer = solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
# [1, 0, 1, 1, 0, 1]
print(answer)