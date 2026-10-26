class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)<=1):
            return 0
        profit=0
        mini=prices[0]
        for i in range(1,len(prices)):
            if(mini>prices[i]):
                mini=prices[i]
            else:
                if(profit<(prices[i]-mini)):
                    profit=prices[i]-mini
        return profit