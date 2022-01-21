class Solution:
    def combine(self, n: int, k: int):
        nums = [x for x in range(1, n + 1)]
        accum = list()
        answer = list()

        def dfs(numbers, accum):
            if len(accum) == k:
                answer.append(accum[:])
                return
            for ind, number in enumerate(numbers):
                accum.append(number)
                numbers_ = numbers[ind:]
                numbers_.remove(number)
                dfs(numbers_, accum)
                accum.pop()

        dfs(nums, accum)


sol = Solution()
answer = sol.combine(4, 2)
print(answer)

