import sys
import collections
input = sys.stdin.readline
num_cities = int(input())
num_nodes = int(input())
graph = list() 
graph_cities = collections.defaultdict(int)

def find(number) : 
    if graph_cities[number] == number : 
        return number
    else : 
        graph_cities[number] = find(graph_cities[number])
        return graph_cities[number] 
def union(start, end) : 
    parent_start = find(start)
    parent_end = find(end)
    if parent_start != parent_end : 
        if parent_start < parent_end : 
            graph_cities[parent_end] = parent_start
        elif parent_start > parent_end : 
            graph_cities[parent_start] = parent_end
def make_answer(answer) :
    for ind, number in enumerate(answer) : 
        if ind == 0 : 
            base = graph_cities[number]
        else : 
            if base != graph_cities[number-1] : 
                return 'NO'
    return 'YES'
for n in range(num_cities) : 
    graph.append(list(input().split()))
    graph_cities[n] = n
for n1 in range(num_cities) : 
    for n2 in range(num_cities) : 
        node = graph[n1][n2]
        if node == '1' : 
            if find(n1) != find(n2) : 
                union(n1, n2)
_answer = map(int, input().split())
answer_ = make_answer(_answer)
if answer_ == 'YES' : 
    print('YES')
else : 
    print('NO')
