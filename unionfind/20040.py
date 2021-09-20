import sys
import collections
n, m = map(int,sys.stdin.readline().rstrip().split())
graph = collections.defaultdict(int)
answer = list() 
def find(number) : 
    return graph[number] 
def union(start, end) : 
    if find(start) != find(end) : 
        if start < end : 
            graph[end] = find(start)
        elif start > end : 
            graph[start] = find(end)
def make_graph(graph) : 
    for ind in range(n) : 
        graph[ind] = ind
make_graph(graph)
for iter in range(m) : 
    start, end = map(int,sys.stdin.readline().rstrip().split())
    if find(start) == find(end) : 
        answer.append(iter + 1)
    union(start, end)
    print(graph)
if len(answer) == 0 :
    print(0)
else : 
    print(min(answer))

    
