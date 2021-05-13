def solution(left, right) : 
    answer = 0 
    result = [0 for _ in range((right - left)+1)]
    for ind, number in enumerate(range(left, right+1)) :  
        for mok in range(1, number + 1) : 
            if number % mok == 0 : 
                result[ind] += 1
    for ind2, number2 in enumerate(result) :
        if number2 % 2 == 0 : 
            answer += range(left, right+1)[ind2]
        else : 
            answer -= range(left, right+1)[ind2]
    return answer
answer = solution(13, 17)
print(answer)