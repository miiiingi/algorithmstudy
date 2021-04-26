class Solution : 
    def combine(self, n , k) : 
        result = [] 
        num = [x for x in range(1, n+1)]
        num_prev = [] 
        def dfs(num) : 
            if len(num) == 2 :
                result.append(num_prev[:])
                num_prev.pop()
            for n in num : 
                num_next = num[:]
                num_next.remove(n)
                num_prev.append(n)
                dfs(num_next)
        dfs(num)
        return result
answer = Solution().combine(4, 2)
print(answer)
