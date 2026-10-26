class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l=0
        dic={}
        k=0
        for i in s:
            if(i in dic):
                l= max(dic[i] +1,l)
            dic[i]=k
            res = max(res, k-l+1)
                
            k=k+1
        return res
            

                