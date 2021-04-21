import functools
def comparison(x, y) : 
    if x + y > y + x : 
        return -1 
    elif x + y < y + x : 
        return 1
    else :
        return 0
def solution(numbers) : 
    numbers = map(str, numbers)
    numlist = [] 
    answer =''
    for number in numbers : 
        numlist.append(number)
    numlist = sorted(numlist, key = functools.cmp_to_key(comparison))
    for number in numlist : 
        answer += number
    if answer < '1' :
        return '0'
    else : 
        return answer
answer = solution([0,0,0,0])
print(answer)