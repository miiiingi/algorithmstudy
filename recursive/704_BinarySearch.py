class Solution:
    def search(self, nums, target) : 
        left = 0
        right = len(nums) - 1
        if not target in nums : 
            return -1
        while left <= right : 
            mid = (left + right) // 2
            if nums[mid] < target : 
                left = mid + 1
            elif nums[mid] > target : 
                right = mid - 1
            else : 
                return mid
        
sol = Solution()
# answer = sol.search([-1, 0, 3, 5, 9 ,12], 9)
answer = sol.search([-1, 0, 5], -1)
# answer = sol.search([-1, 0, 3, 5, 9 ,12], 2)
# answer = sol.search([2, 5], 5)
# answer = sol.search([5], 5)

print(answer)