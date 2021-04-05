# 문제
# 괄호로 된 입력값이 올바른지 판별하라.
# un solved 

def parentheses(s) : 
    stack = [] 
    table = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    for char in s[::-1] : 
        if char not in table.keys() : 
            return False
        elif char in table.keys() : 

        
            pass

    return len(stack) == 0  

answer2 = parentheses('(){}}{')
# print(answer)
print(answer2)