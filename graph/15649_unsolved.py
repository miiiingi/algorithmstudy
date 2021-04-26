N, M = map(int, input().split())
num = [x for x in range(1, N+1)]
result = [] 
num_prev = [] 
def dfs(num) : 
    if len(num_prev) == M :  
        result.append(num_prev[:])
        num_prev.pop()
    for n in num : 
        num_next = num[:]
        num_next.remove(n)
        num_prev.append(n)
        dfs(num_next)
        num_prev.pop()


    return result
answer = dfs(num)
print(answer)