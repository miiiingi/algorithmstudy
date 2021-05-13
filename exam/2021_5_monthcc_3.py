# 1. '110'을 찾자
# 2. 하나씩 넣어보면서 가장 작은수를 반환
import re
def solution(s) : 
    result = [] 
    for strings in s : 
        comp = '1' * len(strings)
        goal = re.sub('110', '', strings)
        for ind in range(len(goal) + 1) : 
            if ind == len(goal) : 
                comp_g = goal + '110'
                if comp > comp_g : 
                    comp = comp_g
            else : 
                comp_g = goal[:ind] + '110' + goal[ind:]
                if comp > comp_g : 
                    comp = comp_g
        result.append(comp)
    return result

# answer = solution(["1110","100111100","0111111010"]) # 한개인경우는 나중에 생각
answer = solution(["0111111010"]) # 한개인경우는 나중에 생각
print(answer)