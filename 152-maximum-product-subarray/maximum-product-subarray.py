class Solution(object):
    def maxProduct(self, nums):
       curmin=nums[0]
       curmax=nums[0]
       result=nums[0]
       for i in range(1,len(nums)):
          num=nums[i]
          if num<0:
             curmax,curmin=curmin,curmax
          curmax=max(num,curmax*num)
          curmin=min(num,curmin*num)
          result=max(result,curmax)
       return result