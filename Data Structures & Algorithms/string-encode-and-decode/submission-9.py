class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            l = len(s)
            res = res + str(l) + "₹" + s
        #print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            
            delimiter = i + s[i:].find("₹")
            #print (delimiter)
            if(s[i:delimiter].isdigit()):
                lenght= len(s[i:delimiter])
                index= int(s[i:delimiter])
                print (index)
                if(index == 0):
                    res.append("")
                    i = i+2
                else :
                    res.append(s[i+1+lenght: index+1+lenght+ i])
                    i = i+ index+1+lenght
            else:
                i=i+1
        return res
