class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == len(t) and s !=t:
            return False
        dp=[0] * (len(s)+1)
        dp[0] = 1
        
        for c in t:
            for i in range(len(s), 0, -1):
                if c == s[i - 1]:
                    dp[i] = dp[i] or dp[i-1]
        if dp[len(s)]: 
            return True
        else:
            return False