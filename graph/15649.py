import sys
sys.setrecursionlimit(10000)
N, M = map(int, input().split())
num = [x for x in range(1, N+1)]
num_prev = [] 
result = [] 
def dfs(num, k) : 
    if k == 0: 
        result.append(num_prev[:])
        return 
    for ind in num : 
        num_next = num[:]
        num_prev.append(ind)
        num_next.remove(ind)
        dfs(num_next, k-1)
        num_prev.pop()
    return result
answer = dfs(num, M)
for s in answer : 
    for ind, x in enumerate(s) : 
        if ind == len(s) - 1 : 
            print(x)
        else : 
            print(x, end= ' ')
    