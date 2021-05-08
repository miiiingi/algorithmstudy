# 어떻게 현재 위치를 나타낼 것인가 ? > 그냥 좌표찍어서 
# 어떻게 2,5,8,0 과의 거리를 계산할 것 인가?

import collections
def update(state) : 
    if state == 1 :
        return (1, 1)
    if state == 2 :
        return (1, 2)
    if state == 3 :
        return (1, 3)
    if state == 4 :
        return (2, 1)
    if state == 5 :
        return (2, 2)
    if state == 6 :
        return (2, 3)
    if state == 7 :
        return (3, 1)
    if state == 8 :
        return (3, 2)
    if state == 9 :
        return (3, 3)
    if state == '*' :
        return (4, 1)
    if state == 0 :
        return (4, 2)
    if state == '#' :
        return (4, 3)
def distance(current, hand) : 
    distance_L_w = abs(current[0]-hand[0][0])
    distance_L_h = abs(current[1]-hand[0][1])
    distance_R_w = abs(current[0]-hand[1][0])
    distance_R_h = abs(current[1]-hand[1][1])
    return distance_L_w + distance_L_h, distance_R_w + distance_R_h
def solution(numbers, hand) : 
    numbers = collections.deque(numbers)
    result = [] 
    position_hand = [[4, 1], [4, 3]]
    while numbers : 
        number = numbers.popleft()
        if number == 1  or number == 4 or number == 7 : 
            position_hand[0] = update(number)
            result.append('L')
        elif number == 3 or number == 6 or number == 9 : 
            position_hand[1] = update(number)
            result.append('R')
        else : 
            position_current = update(number)
            distance_L, distance_R = distance(position_current, position_hand)
            if distance_L < distance_R :
                position_hand[0] = position_current
                result.append('L')
            if distance_R < distance_L :
                position_hand[1] = position_current
                result.append('R')
            if distance_R == distance_L :
                if hand == 'left' :  
                    position_hand[0] = position_current
                    result.append('L')
                if hand == 'right' :  
                    position_hand[1] = position_current
                    result.append('R')
    answer = ''
    for r in result : 
        answer += r
    return answer 
answer = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')
print(answer)
