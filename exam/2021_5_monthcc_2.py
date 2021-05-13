# 1. 수를 비트연산으로 바꾸면서
# 2. 다른 지점을 하나씩 구해서
# 3. 1, 2 가 나오면 바로 retrun
def solution(numbers) : 
    result = [] 
    for number in numbers : 
        comp = bin(number)[2:]
        while True : 
            comp_number = 0 
            number += 1
            comp_new = bin(number)[2:]
            length = len(comp_new) - len(comp)
            if length > 0  : 
                comp = '0' * length + comp
                for x, y in zip(comp_new, comp) : 
                    if x != y : 
                        comp_number += 1
                if comp_number <= 2 : 
                    result.append(number)
                    break
            else : 
                for x, y in zip(comp_new, comp) : 
                    if x != y : 
                        comp_number += 1
                if comp_number <= 2 : 
                    result.append(number)
                    break
    return result 
answer = solution([2, 7])
print(answer)