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
    for x in num : 
        num_next = num[:]
        num_prev.append(x)
        # num_next.remove(ind)
        dfs(num_next, k-1)
        num_prev.pop()
    return result
answer = dfs(num, M)
for s in answer : 
    answer = ''
    for ind in range(len(s)) : 
        if ind == len(s) - 1 : 
            answer = answer + str(s[ind])
        else : 
            answer = answer + str(s[ind]) + ' '
    print(answer)

    