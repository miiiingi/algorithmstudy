import collections
def solution(n, lost, reserve) : 
    lost = collections.deque(lost)
    reserve = collections.deque(reserve)
    length_lost = len(lost)
    reserve_lost = [] 
    for ind in range(len(reserve)) : 
        people_reserve = reserve[ind]
        if people_reserve in lost :  
            lost.remove(people_reserve)
            reserve_lost.append(people_reserve)
            length_lost -= 1
    for people_reservelost in reserve_lost : 
        reserve.remove(people_reservelost)
    while reserve : 
        people_reserve = reserve.popleft()
        for ind, people_lost in enumerate(lost) : 
            if (people_lost - 1) == people_reserve or (people_lost + 1) == people_reserve :
                length_lost -= 1
                del lost[ind]
                break
    return n - length_lost
answer = solution(5, [2, 3, 4], [1, 2, 3])
print(answer)

