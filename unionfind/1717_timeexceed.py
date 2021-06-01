import sys
sys.setrecursionlimit(10**5)

N, M = map(int,sys.stdin.readline().rstrip().split())
parent = [-1 for _ in range(N+1)]
def union(a,b) : 
    a = find(a)
    b = find(b)
    if a != b : 
        parent[a] = b

def find(a) : 
    if parent[a] == -1 : 
        return a
    else :
        parent[a] = find(parent[a])
        return parent[a]

for i in range(M) : 
    operation, a, b = map(int, input().split())
    if operation == 0 :
        union(a,b)
    elif operation == 1 : 
        if find(a) == find(b) : 
            print('YES')
        else : 
            print('NO')
