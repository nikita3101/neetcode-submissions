class Solution:
    def firstUniqChar(self, s: str) -> int:
        i =0
        for c in s:
            if(c not in s[:i] and c not in s[i+1:]):
                return i
            i = i+1
        return -1