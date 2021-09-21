import sys
import collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = collections.defaultdict(int)
answer = list() 
def find(number) : 
    if graph[number] == number : 
        return number
    else : 
        graph[number] = find(graph[number])
        return graph[number] 
def union(start, end) : 
    parent_start = find(start)
    parent_end = find(end)
    if parent_start != parent_end : 
        if parent_start < parent_end : 
            graph[parent_end] = parent_start
        elif parent_start > parent_end : 
            graph[parent_start] = parent_end
def make_graph(graph) : 
    for ind in range(n) : 
        graph[ind] = ind
make_graph(graph)
for iter in range(m) : 
    start, end = map(int, input().split())
    if find(start) == find(end) : 
        answer.append(iter + 1)
    union(start, end)
if len(answer) == 0 :
    print(0)
else : 
    print(min(answer))