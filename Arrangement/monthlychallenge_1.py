def solution(ab, signs) : 
    answer = 0 
    for value, sign in zip(ab, signs) :
        if sign : 
            answer += value 
        else : 
            answer -= value
    return answer