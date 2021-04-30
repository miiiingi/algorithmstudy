class Solution : 
    result = [] 
    def combinationSum(self, candidates, target) : 
        self.dfs(candidates, target)
        return self.result
    def dfs(self, candidates, target) : 
        pass