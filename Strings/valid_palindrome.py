# 1. 대소문자를 구별하지 않고, 특수문자와 띄어쓰기를 고려하지 않는 문자열을 만든다.
# 2. 앞에서부터 시작하고 뒤에서부터 시작하면서 하나씩 비교해서 다를 경우 False를 출력하고 모두 같은 경우 True를 출력
def check(strings) : 
    answer = True
    comp1 = [s.lower() for s in strings if s.isalnum() == True]
    for x, y in zip(comp1, comp1[::-1]) :  
        if x != y : 
            return False
    return answer
answer = check('A man, a plan, a canal: Panama')
answer2 = check('race a car')
print(answer2)