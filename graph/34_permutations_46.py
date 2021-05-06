class Solution : 
    result = [] 
    element_prev = []
    def permute(self, num) : 
        self.dfs(num)
        return self.result
    def dfs(self, elements) :  
        if len(elements) == 0 :
            self.result.append(self.element_prev[:])
        for e in elements : 
            element_next = elements[:]
            element_next.remove(e)
            self.element_prev.append(e)
            self.dfs(element_next)
            self.element_prev.pop()

answer = Solution().permute([1,2,3])
print(answer)