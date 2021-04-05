# 문제
# 괄호로 된 입력값이 올바른지 판별하라.

# 전략 
# 일단 짝을 맞춰주는 게 중요하니까, 정해진 짝을 O(1)에 꺼내쓸 수 있는 딕셔너리로 키 밸류 값을 정해주자.
# 그리고 키에 있는 것들만 append하고, 키에 없는 것들이랑 마지막 키에 대한 밸류값이 일치하지 않는 것은 모두 False로 처리
# 그리고 키 들만 있는 것들도 False로 처리
# 일반적인 아이디어는 떠올리는 것이 그렇게 어렵지 않은 문제지만, 예외처리랑 신경쓸 것이 많아서 어렵게 느껴짐!

def parentheses(s) : 
    stack = [] 
    table = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    for char in s : 
        if char in table.keys() : 
            stack.append(char)
        elif not stack or table[stack[-1]] != char : 
            return False
        elif table[stack[-1]] == char : 
            stack.pop()

    return len(stack) == 0 

answer = parentheses('()')
print(answer)