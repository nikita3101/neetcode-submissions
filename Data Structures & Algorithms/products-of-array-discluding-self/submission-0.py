class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            if(i != len(nums)-1):
                right[i] = right[i+1] * nums[i+1]
        #print(right)
        i=0
        prod = 1
        for n in nums:
            if(i != 0):
                right[i] = prod * right[i]
            prod = prod * nums[i]
            i = i + 1
        return right

        