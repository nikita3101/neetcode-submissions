class Solution: 
    def findMin(self, nums: List[int]) -> int:
      low = 0
      high = len(nums) - 1
      if(len(nums)==1):
         return nums[0]
      if(nums[low] < nums[high]):
         return nums[low]
      mid = (low + high) // 2
      while low < high:
         mid = (low + high) // 2
         #print(str(low) + str(high))
         if(nums[mid] > nums[low]):
            low = mid
         else:
            high = mid
      return nums[low+1]

        