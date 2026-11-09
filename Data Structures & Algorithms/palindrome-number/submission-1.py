class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        l = 0
        r = len(strx) -1
        while l <= r:
            if (strx[l]==strx[r]):
                l = l+1
                r = r-1
            else:
                return False
        return True