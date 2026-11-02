class Solution:
    def firstUniqChar(self, s: str) -> int:
        cdict = {}
        i =0
        for c in s:
            if(c not in cdict):
                cdict[c] = i
            else:
                cdict[c] =-1
            i = i+1
        for (l,v) in cdict.items():
            if v != -1:
                return v
        return -1