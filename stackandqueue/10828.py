import sys
import collections
input = sys.stdin.readline
N = int(input())
array = collections.deque()
answer = list()
for _ in range(N) : 
    inputs = input()
    for ind, x in enumerate(inputs.split()) : 
        if ind == 0 : 
            oper = x
            if x == 'push' : 
                pass
            else : 
                continue
        elif ind == 1 : 
            number = x
    if oper == 'push' : 
        array.append(number)
    elif oper == 'top' : 
        if len(array) != 0 : 
            answer.append(array[-1])
        else : 
            answer.append(-1)
    elif oper == 'size' : 
        answer.append(len(array))
    elif oper == 'empty' : 
        if len(array) == 0 : 
            answer.append(1)
        else : 
            answer.append(0)
    elif oper == 'pop' : 
        if len(array) != 0 : 
            pops = array.pop()
            answer.append(pops)
        else : 
            answer.append(-1)
for a in answer : 
    print(a)