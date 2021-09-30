import sys
import collections
input = sys.stdin.readline
N = int(input())
answer_all = list()
for _ in range(N) : 
    n, question = map(int, input().split())
    importance = list(map(int, input().split()))
    document = collections.deque()
    answer = list()
    for _n, i in zip(range(n), importance) : 
        document.append((_n, i))
    while len(document) > 1 : 
        pops = document.popleft()
        count = 0 
        comp = max(document, key = lambda x : x[1])[1]
        if pops[1] >= comp : 
            answer.append(pops)
        else : 
            document.append(pops)
    else : 
        pops = document.pop()
        answer.append(pops)
    for ind, a in enumerate(answer) : 
        if a[0] == question : 
            answer_all.append(ind + 1)
            break
for x in answer_all : 
    print(x)
