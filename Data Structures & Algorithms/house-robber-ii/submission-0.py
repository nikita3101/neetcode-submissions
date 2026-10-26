class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums) -> int:
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])
            i =2
            while i < len(nums):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
                i = i +1
            return dp[len(nums)-1]
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))

        