def solution(numbers) : 
    print(sorted(numbers, key = lambda x : x[0], reverse=True))
    answer =''
    return answer 
answer = solution([6, 10, 2])
print(answer)