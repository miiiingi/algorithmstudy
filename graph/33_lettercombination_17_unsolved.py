class Solution : 
    def letterCombinations(self, digits) : 
        def dfs(index, path) :
            if len(path) == len(digits) :
                result.append(path)
                return
            for i in range(index, len(digits)) : 
                # 여기서 중요한 것은 digits을 반복하는데, 반복할 때, 이전의 문자를 붙잡아놓고 뒤의 문자를 반복시키는 것 !
                for j in graph[digits[i]] : 
                    dfs(i+1, path+j)
        graph ={'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' :'jkl', '6' : 'mno', '7' :'pqrs', '8' :'tuv', '9':'wxyz'}
        result = [] 
        dfs(0, '') 

        return result 
answer = Solution().letterCombinations(digits= '23')
print(answer)
