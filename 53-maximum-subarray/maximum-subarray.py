class Solution(object):
    def maxSubArray(self, nums):
       currsum=0
       maxsum=float('-inf')
       for i in nums:
        currsum+=i
        maxsum=max(currsum,maxsum)
        if currsum<0:
            currsum=0
       return maxsum