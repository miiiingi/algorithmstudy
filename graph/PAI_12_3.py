class Solution:
    def permute(self, nums):
        answer = list()
        accum = list()

        def dfs(numbers, accum):
            if len(accum) == len(nums):
                answer.append(accum[:])
                return

            for number in numbers:
                accum.append(number)
                numbers_ = numbers[:]
                numbers_.remove(number)
                dfs(numbers_, accum)
                accum.pop()

        dfs(nums, accum)

sol = Solution()
answer = sol.permute([1, 2, 3])

