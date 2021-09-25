import sys
import collections
input = sys.stdin.readline
N = int(input())
array = collections.deque(input().split())
answer = ''
for _ in range(len(array)) :
    number = array.popleft()
    _answer = collections.deque() 
    for x in array : 
        if number < x : 
            _answer.append(x)
            break
    if len(_answer) == 0 : 
        answer += '-1 '
    else : 
        answer += f'{_answer.popleft()} '
answer = answer.strip()
print(answer)


