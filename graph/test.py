def solution(n) : 
    answer = 0 
    list_number = [x for x in range(1, n+1)]
    for ind_start in range(n) : 
        for ind_end in range(n) : 
            if sum(list_number[ind_start : ind_end+1]) == n : 
                answer += 1
                break
            elif sum(list_number[ind_start : ind_end+1]) > n  : 
                break
    return answer
answer = solution(15)
print(answer)