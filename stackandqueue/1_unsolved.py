import collections
def solution(bridge_length, weight, truck_weights) : 
    count_whole = 0
    number_truck = len(truck_weights)
    transiting = collections.deque([])
    truck_weights = collections.deque(truck_weights)
    truck_finish = []
    while True :
        if len(truck_weights) == 0 and len(truck_finish) == number_truck : 
            break
        else : 
            if len(truck_weights) != 0 : 
                if sum(item[1] for item in transiting) + truck_weights[0] <= weight : 
                    truck = truck_weights.popleft()
                    if transiting : 
                        for number in range(len(transiting)) : 
                            transiting[number][0] += 1
                    transiting.append([1, truck])
                    for number in range(len(transiting)) : 
                        if transiting[number][0] >= bridge_length :
                            truck_finish.append(transiting.popleft())
                    count_whole += 1

                            # truck = truck_weights.popleft()
                            # count_whole += 1
                            # transiting.append([1, truck])
                        # else : 
                        #     transiting[number][0] += 1
                        #     count_whole += 1
                else : 
                    # count_overbridge_length = 0
                    for number in range(len(transiting)) : 
                        if transiting[number][0] >= bridge_length :
                            truck_finish.append(transiting.popleft())
                            truck = truck_weights.popleft()
                            count_whole += 1
                            transiting.append([1, truck])
                        else : 
                            transiting[number][0] += 1
                            count_whole += 1
                    # for _ in range(count_overbridge_length) :   
                    #     truck_finish.append(transiting.popleft())
            else : 
                    count_overbridge_length = 0
                    for number in range(len(transiting)) : 
                        if transiting[number][0] >= bridge_length :
                            count_overbridge_length += 1
                        else : 
                            transiting[number][0] += 1
                            count_whole += 1
                    for _ in range(count_overbridge_length) :   
                        truck_finish.append(transiting.popleft())
    return count_whole

answer = solution(2, 10, [7, 4, 5, 6])
print(answer)
