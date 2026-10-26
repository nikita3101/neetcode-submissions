class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if( len(s) != len(t)):
            return False
        else:
            hashmap = {}
            for i in s:
                if i in hashmap:
                    hashmap[i] += 1
                else:
                    hashmap[i] = 1
            #print(hashmap)
            for j in t:
                if j not in hashmap:
                    return False
                else:
                    hashmap[j] -= 1
            #print(hashmap)
            for value in hashmap.values():
                if(value != 0):
                    return False
            return True