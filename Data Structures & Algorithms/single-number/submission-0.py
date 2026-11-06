class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        else:
            res = nums[0]
            for n in nums[1:]:
                res = res ^ n
            return res