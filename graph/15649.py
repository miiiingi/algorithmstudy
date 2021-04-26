N, M = map(int, input().split())
num = [x for x in range(1, N+1)]
result = [] 
num_prev = [] 
def NM(num, M) : 
    def dfs(num) : 
        for n in num : 
            num_next = num[:]
            num_next.remove(n)
            num_prev.append(n)
            if len(num_prev) != M :  
                result.append(num_prev)
            dfs(num_next)
answer = NM(num, N)
print(answer)