import collections
class truck : 
    list_transited = [] 
    list_transiting = [] 
    def untransiting(self, truck) : 
        # 다리를 지나지 않은 트럭을 저장하는 역할, 트럭이 다리를 지날지 말지에 대한 무게를 전달하는 역할
        return
    def transiting(self, trucklist, untransiting, weight) : 
        sum_truck = 0
        # 다리를 지나는 트럭을 저장하는 역할, 다리를 지나고 있는 트럭의 무게를 전달하는 역할
        for t in trucklist : 
            sum_truck += t[0]
        if sum_truck + untransiting[0] < weight : 
            return 1
        return
    def transited(self, truck) :  
        # 다리를 지난 트럭을 저장하는 역할
        return
def solution(bridge_length, weight, truck_weights) : 
    time = 0
    number_complete = len(truck_weights)
    list_untransiting = collections.deque(truck_weights)
    while True : 
        if len(truck.list_transited) == number_complete :  
            break
        else : 
            return
    print(truck.list_transited)
    exit()

    return
answer = solution(2, 10, [7, 4, 5, 6])
print(answer)