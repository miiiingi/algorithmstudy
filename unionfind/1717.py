import sys
sys.setrecursionlimit(10**6)
n, m = map(int,sys.stdin.readline().split())
nodes = [0] * (n+1)
for node in range(n+1) :
    nodes[node] = node

def union(a, b) : 
    parent_a, parent_b = find(a), find(b)
    if parent_a != parent_b : 
        if parent_a > parent_b : 
            nodes[parent_a] = parent_b
        elif parent_a < parent_b : 
            nodes[parent_b] = parent_a

def find(number) : 
    if nodes[number] == number : 
        return number
    else : 
        nodes[number] = find(nodes[number])
        return nodes[number]

for iter in range(m) : 
    operation, a, b = map(int,sys.stdin.readline().split())
    if operation == 0 : 
        union(a, b)
    elif operation == 1 : 
        parent_a, parent_b = find(a), find(b)
        if parent_a == parent_b : 
            print('YES')
        else: 
            print('NO')
    print(nodes)