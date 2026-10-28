class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack =deque()
        maxprofit=0
        for i in range(len(prices)-1, -1, -1):
            if len(stack)> 0 and prices[i] < stack[-1]:
                if(maxprofit < stack[-1]-prices[i]):
                    print(stack[-1])
                    print(prices[i])
                    maxprofit=stack[-1]-prices[i]
            else:
                stack.append(prices[i])
        return maxprofit
        