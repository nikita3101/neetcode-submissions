class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        for c in s:
            if c in dic:
                dic[c]+=1
            else:
                dic[c]=1
        for c in t:
            if c in dic:
                dic[c]=dic[c]-1
            else:
                return False
        for v in dic.values():
            if(v!=0):
                return False
        return True
