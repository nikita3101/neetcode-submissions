class Solution:
    def countBits(self, n: int) -> List[int]:
        def getbitcount(val) -> int:
            count =0
            while val>0:
                r = val % 2
                if r == 1:
                    count = count + 1
                val = val//2
            return count
        res = []
        i = 0
        for i in range(n+1):
            res.append(getbitcount(i))
        return res
