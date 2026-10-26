class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i =0
        m = len(word1)
        n = len(word2)
        for i in range(min(n,m)):
            res = res + word1[i] + word2[i]
        if(m>n):
            res = res +word1[i+1:]
        else:
            print(res)
            res = res + word2[i+1:]
        return res