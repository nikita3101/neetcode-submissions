class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i]=1
        #print(dic)
        dic={ke:v for ke, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
        #print(dic)
        res=[]
        for key,v in enumerate(dic):
            res.append(v)
        return res[:k]
