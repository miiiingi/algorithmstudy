import collections
def solution(bridge_length, weight, truck_weights) : 
    time = 0
    number_complete = len(truck_weights)
    list_untransiting = collections.deque(truck_weights)
    list_transiting = collections.deque([])
    list_transited = collections.deque([])

    while True : 
        number_complete_truck = 0 
        number_sumof_transiting = 0
        if len(list_transited) == number_complete :  
            break
        else : 
            time += 1
            for transiting in list_transiting : 
                if transiting[1] == bridge_length : 
                    number_complete_truck += 1
            for number_iter in range(number_complete_truck) : 
                list_transited.append(list_transiting.popleft())
            for transiting in list_transiting : 
                number_sumof_transiting += transiting[0]

            if list_untransiting : 
                if number_sumof_transiting + list_untransiting[0] <= weight : 
                    list_transiting.append([list_untransiting.popleft(), 0])
            for transiting in list_transiting : 
                transiting[1] += 1
    return time
answer = solution(100, 100, [10 for _ in range(10)])
print(answer)