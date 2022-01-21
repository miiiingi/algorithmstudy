class Solution:
    def letterCombinations(self, digits: str):
        answer = list()
        accum = list()
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(numbers, accum):
            if len(accum) == len(digits):
                answer.append(accum[:])
                return
            for ind, digit in enumerate(numbers):
                for let in letters[digit]:
                    accum.append(let)
                    dfs(numbers[ind + 1 :], accum)
                    accum.pop()
        dfs(digits, accum)
        answer_ = list()
        for word in answer :
            accum = ''
            for w in word : 
                accum += w
            answer_.append(accum)
        print(answer_) 




sol = Solution()
answer = sol.letterCombinations("23")
print(answer)
