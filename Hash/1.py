import collections
from typing import Collection

def solution1(participant, completion) : 
    _answer = 0 
    for p in participant :
        _answer += hash(p)
    for c in completion : 
        _answer -= hash(c)
    for a in participant : 
        if hash(a) == _answer : 
            return a

def solution2(participant, completion) : 
    _answer  = collections.Counter(participant) - collections.Counter(completion)
    return list(_answer.keys())[0]

participant = ['mislav','stanko','ana', 'mislav']
completion = ['stanko', 'ana', 'mislav']
answer1 = solution1(participant, completion)
answer2 = solution2(participant, completion)
print(answer1, answer2)