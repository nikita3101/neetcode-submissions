class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for a in range(1, len(nums)+1):
            res = res ^ a
        for n in nums:
            res = res ^ n
        return res
        