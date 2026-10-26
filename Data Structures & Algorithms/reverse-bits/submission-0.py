class Solution:
    def reverseBits(self, n: int) -> int:
        k=31
        res = 0
        print(str(n))
        while n > 0:
            r = n%2
            if(r == 1):
                res = res + pow (2, k)
                print(res)
            k = k -1 
            n = n//2
        return res

        