class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        se = set(nums)
        length = 1
        maxlen= length
        for n in nums:
            if n in se and n-1 not in se:
                length = 1
                t = n+1
                while t in se: 
                    length += 1
                    t =  t + 1
                if maxlen < length:
                    maxlen= length
            else:
                length = 1
        return maxlen
            

            
        