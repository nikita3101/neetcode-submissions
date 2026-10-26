class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        i=0
        for n in nums:
            if target-n in hashmap and i != hashmap.get(target-n):
                return [hashmap.get(target-n),i]
            hashmap[n] = i
            i = i + 1
        return []
