import sys
import collections
input = sys.stdin.readline
N = int(input())
array = collections.deque()
array_answer = list()
for _ in range(N) : 
    operation = input()
    for ind, x in enumerate(operation.split()) : 
        if ind == 0 :
            operation = x
        elif ind == 1 : 
            number = int(x)
    if operation == 'push_back' : 
        array.append(number)
    elif operation == 'push_front' :
        array.appendleft(number)
    elif operation == 'pop_front' : 
        if array : 
            array_answer.append(array.popleft())
        else : 
            array_answer.append(-1)
    elif operation == 'pop_back' : 
        if array : 
            array_answer.append(array.pop())
        else : 
            array_answer.append(-1)
    elif operation == 'size' : 
        array_answer.append(len(array))
    elif operation == 'empty' : 
        if array : 
            array_answer.append(0)
        else : 
            array_answer.append(1)
    elif operation == 'front' : 
        if array : 
            array_answer.append(array[0])
        else : 
            array_answer.append(-1)
    elif operation == 'back' : 
        if array : 
            array_answer.append(array[-1])
        else : 
            array_answer.append(-1)
for x in array_answer : 
    print(x)
