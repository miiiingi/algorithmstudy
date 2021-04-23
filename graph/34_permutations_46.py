# 재귀를 직관적으로 이해할 수 있는 사고력 기르기 !! 복습 필수 !!
class Solution : 
    def permute(self, num) : 
        result = [] 
        element_prev = []
        def dfs(elements) :  
            if len(elements) == 0 :
                result.append(element_prev[:])
            for e in elements : 
                element_next = elements[:]
                element_next.remove(e)
                element_prev.append(e)
                dfs(element_next)
                element_prev.pop()
        dfs(num)
        return result
answer = Solution().permute([1,2,3])
print(answer)