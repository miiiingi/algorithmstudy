# 예외 0, -1
import collections
def solution(s) : 
    count = 0
    strings =collections.deque(s)
    base = {'{' : '}', '[' : ']', '(' : ')'}
    for iter in range(len(strings)) : 
        stack = [] 
        count_stack = 0
        if iter >= 1 : 
            elem = strings.popleft()
            strings.append(elem)
        for comp in strings : 
            if comp in base.keys() : 
                stack.append(comp)
            else : 
                if stack and base[stack[-1]] == comp : 
                    stack.pop()
                    count_stack += 1
                else : 
                    continue
        if len(stack) == 0 and count_stack != 0:
            count += 1
    return count 
answer = solution(')))')
print(answer)