class Solution : 
    def combine(self, N , k) : 
        result = [] 
        num = [x for x in range(1, N+1)]
        num_prev = [] 
        def dfs(num, start, k) : 
            if k == 0 :
                result.append(num[:])
            element = num[start:]

        dfs(num, 0, k)
        return result
answer = Solution().combine(4, 2)
print(answer)
