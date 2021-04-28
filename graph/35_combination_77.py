class Solution : 
    result = [] 
    num_prev = [] 
    def combine(self, n , k) : 
        self.num = [x for x in range(1, n+1)]
        self.dfs(self.num, 0, k)
        return self.result

    def dfs(self, num, start, k) : 
        if k == 0 :
            self.result.append(self.num_prev[:])
            return
        for ind in range(start, len(num)) : 
            self.num_prev.append(num[ind])
            self.dfs(num, ind+1, k-1)
            self.num_prev.pop()

answer = Solution().combine(4, 2)
print(answer)
