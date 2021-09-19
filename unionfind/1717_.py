import collections
import sys
def union(a, b) : 
    parent_a, parent_b = find(a), find(b)
    if parent_a != parent_b : 
        if a > b : 
            nodes[b] = a
        elif a < b : 
            nodes[a] = b

def find(number) : 
    if nodes[number] == number : 
        return number
    else : 
        nodes[number] = find(nodes[number])
        return nodes[number]

n, m = map(int,sys.stdin.readline().rstrip().split())
nodes = collections.defaultdict(int)
for node in range(m+1) :
    nodes[node] = node
for iter in range(m) : 
    operation, a, b = map(int,sys.stdin.readline().rstrip().split())
    if operation == 0 : 
        union(a, b)
    elif operation == 1 : 
        parent_a, parent_b = find(a), find(b)
        if parent_a == parent_b : 
            print('YES')
        else: 
            print('NO')