import collections
iter = int(input())
for i in range(iter) : 
    number_student = int(input())
    couple = [] 
    for x in map(int, input().split()) :
        couple.append(x)
    graph = collections.defaultdict(int)
    for m, c in zip(range(number_student), couple) : 
        graph[m+1] = c
    