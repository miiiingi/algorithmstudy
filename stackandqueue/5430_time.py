import sys 
import collections
input = sys.stdin.readline
N = int(input())
for _ in range(N) : 
    oper = collections.deque(input().strip())
    n = int(input())
    array = input().strip()
    array = array.strip('[')
    array = array.strip(']')
    if not array : 
        print('error')
        continue
    else : 
        array = collections.deque(map(int, array.split(',')))
    while oper : 
        pops = oper.popleft()
        if pops == 'R' : 
            array_ = collections.deque()
            while array : 
                array_.append(array.pop())
            array = array_
        elif pops == 'D' : 
            if not array : 
                print('error')
                break 
            else :  
                array.popleft()
    if array : 
        print(list(array))
