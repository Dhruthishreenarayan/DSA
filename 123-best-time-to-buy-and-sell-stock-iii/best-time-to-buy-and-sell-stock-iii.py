class Solution(object):
    def maxProfit(self, prices):
        best1=float('-inf')
        sell1=0
        best2=float('-inf')
        sell2=0
        for price in prices:
            best1=max(best1,-price)
            sell1=max(sell1,best1+price)
            best2=max(best2,sell1-price)
            sell2=max(sell2,best2+price)
        return sell2
        