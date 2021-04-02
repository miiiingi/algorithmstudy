def solution(array , commands) : 
    answer = [] 
    for _array in commands : 
        array_ = array[_array[0]-1 : _array[1]]
        array_ = sorted(array_)
        _answer = array_[_array[2]-1]
        answer.append(_answer)
    return answer 

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = solution(array, commands)
print(answer)
