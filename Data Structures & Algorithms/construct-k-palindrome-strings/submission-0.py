class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        count = [0] *26
        for c in s:
            count[ord(c)-97] += 1
        s=0
        for x in count:
            if(x%2!=0):
                s = s+1
        if(s<=k):
            return True
        else:
            return False
