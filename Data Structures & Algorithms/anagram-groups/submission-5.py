class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getbitarray(s: str) -> str:
            arr = [0] * 26
            for i in s:
                #print(ord(i)-97)
                arr[ord(i)-97] = arr[ord(i)-97] + 1
            #print(arr)
            return '.'.join(str(a) for a in arr)
        res = []
        hashmap = {}
        for s in strs:
            arr = getbitarray(s)
            #print(s + " : " + arr)
            if arr in hashmap:
                hashmap[arr].append(s)
            else:
                hashmap[arr] = [s]
        #print(hashmap)
        for value in hashmap.values():
            res.append(value)
        return res

