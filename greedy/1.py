import collections
def solution(n, lost, reserve) : 
    num_lost = len(lost)
    lost = collections.deque(lost)
    reserve = collections.deque(reserve)
    while lost : 
        people = lost.popleft()
        for ind, people2 in enumerate(reserve) : 
            if people - 1 == people2 or people + 1 == people2 or people == people2:
                del reserve[ind] 
                num_lost -= 1
                break 
    return n - num_lost
answer = solution(30, [x for x in range(1, 31)], [1])
print(answer)

