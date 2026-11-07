class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = Counter(magazine)
        dic1= Counter(ransomNote)
        for c,i in dic1.items():
            if(c not in dic):
                return False
            elif(i<=dic[c]):
                dic[c] -= 1
            else:
                return False
        return True
