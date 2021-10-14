class Solution:
    def maxProfit(self, prices) -> int:
        stack = list()
        answer = 0 
        for s in prices : 
            while stack and stack[-1] < s : 
                answer += (s - stack[-1])
                break
            stack.append(s)
        return answer
sol = Solution()
answer = sol.maxProfit([7,1,5,3,6,4,])
print(answer)



        