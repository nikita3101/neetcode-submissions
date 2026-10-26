class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    res.add(tuple([nums[i],nums[j], nums[k]]))
                    j = j+1
                    k = k-1
                elif nums[j] + nums[k] > -1 * nums[i]:
                    k = k - 1
                else:
                    j = j + 1
        return [list(i) for i in res]

