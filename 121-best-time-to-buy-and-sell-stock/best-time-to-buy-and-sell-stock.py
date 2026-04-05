class Solution(object):
    def maxProfit(self, prices):
       maxprofit=0
       bestbuy=prices[0]
       for i in prices:
        if i > bestbuy:
            maxprofit=max(maxprofit,i-bestbuy)
        bestbuy=min(bestbuy,i)
       return maxprofit
        