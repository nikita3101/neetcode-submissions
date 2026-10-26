class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextgrater = [0] * len(nums2)
        res = [-1] * len(nums1) 
        stack = deque()
        for j in range(len(nums2)-1, -1, -1):
            if(j == len(nums2)-1):
                nextgrater[j] = -1
                stack.append(nums2[j])
            else:
                if(nums2[j] > stack[-1]):
                    k = j
                    while (len(stack)>0 and nums2[k] > stack[-1]):
                        stack.pop()
                    if stack:
                        nextgrater[j] = stack[-1]
                    else:
                        nextgrater[j] = -1
                    stack.append(nums2[j])
                    
                else:
                    nextgrater[j] = stack[-1]
                    stack.append(nums2[j])
        dic = {}
        for j in range(len(nums2)):
            dic[nums2[j]] = j
        i = 0
        for i in range(len(nums1)):
            if nums1[i] in dic:
                res[i] = nextgrater[dic[nums1[i]]]
            else:
                res [i] = -1
        return res


