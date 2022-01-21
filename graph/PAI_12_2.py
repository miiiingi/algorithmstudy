class Solution:
    def letterCombinations(self, digits: str):
        answer = list()
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
        length = len(digits)
        accum = list()

        def dfs(digits, accum):
            if len(accum) == length:
                answer.append(accum[:])
                accum.pop()
                return
            for ind, digit in enumerate(digits):
                for let in letters[digit]:
                    accum.append(let)
                    dfs(digits[ind + 1 :], accum)
                accum.pop()

        dfs(digits, accum)
        print(answer)


sol = Solution()
answer = sol.letterCombinations("23")
print(answer)
