class Solution : 
    result = [] 
    list_sum = [] 
    def combinationSum(self, candidates, target) : 
        self.dfs(candidates, target)
        return self.result
    def dfs(self, candidates, target) : 
        for ind in range(len(candidates)) : 
            self.list_sum.append(candidates[ind])
            if sum(self.list_sum) > target : 
                self.list_sum.pop()
                return
            elif sum(self.list_sum[:]) == target : 
                self.result.append(self.list_sum[:])
                return
            self.dfs(candidates, target)
            self.list_sum.pop()
answer = Solution().combinationSum([2,3,6,7], 7)
print(answer)