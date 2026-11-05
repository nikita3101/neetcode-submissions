class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
           
            while(len(stack)!=0 and temperatures[i] >= stack[-1][0]):
                stack.pop()
            #print(stack)
            if(len(stack)!=0):
                res[i] = stack[-1][1] - i
            stack.append((temperatures[i],i))
            #print(res)
        return res