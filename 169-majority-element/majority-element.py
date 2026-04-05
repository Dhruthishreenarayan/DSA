class Solution(object):
    def majorityElement(self, nums):
         freq=0
         n=len(nums)
         ans=0
         for i in range(n):
            if freq==0:
              ans=nums[i]
            if ans==nums[i]:
                freq+=1
            else :
                freq-=1
         return ans
        