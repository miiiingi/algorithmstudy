def count(array, answers) : 
    _count = 0 
    for x, y in zip(array, answers) :  
        if x == y : 
            _count += 1
    return _count

def make_strings(array, answers) : 
    len_answers = len(answers)
    mok = len_answers // len(array)
    if mok == 0 :
        array_ = array[:(len_answers % len(array))]
    else : 
        array_ = array * mok + array[:(len_answers % len(array))]
    return array_

def solution(answers) : 
    answer = [] 
    len_answers = len(answers)
    _first = [1,2,3,4,5]
    _second = [2,1,2,3,2,4,2,5]
    _third = [3,3,1,1,2,2,4,4,5,5]
    first = make_strings(_first, answers)
    second = make_strings(_second, answers)
    third = make_strings(_third, answers)
    num_first = count(first, answers)    
    num_second = count(second, answers)    
    num_third = count(third, answers)    
    num_max = max(num_first, num_second, num_third)
    num_list = [num_first, num_second, num_third]
    for ind, x in enumerate(num_list) : 
        if x == num_max : 
            answer.append((ind+1))
    return sorted(answer) 

def solution2(answers) : 
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

answer = solution([1,3,2,4,2])
answer2 = solution2([1,3,2,4,2])
print(answer2)