import collections
# 문제
# 중복된 문자를 제외하고 사전식 순서로 나열하라.

# 전략
# 문자를 하나씩 받으면서 하나씩 크기를 비교해서 감소하는 순서이면 넘기고 증가하는 순서이면 계속 stack에 쌓자.
# un solved

def remove(s) : 
    stack = [] 
    for char in s : 
        if not stack : 
            stack.append(char)
        else : 
            if stack[-1] < char : 
                stack.append(char)
            elif stack[-1] > char : 
                stack.pop()
                stack.append(char)
    return stack
        

answer = remove('bcabc')
print(answer)
