class Solution(object):
    def singleNumber(self, nums):
       n=len(nums)
       ans=0
       for i in nums:
        ans=ans^i
       return ans
        