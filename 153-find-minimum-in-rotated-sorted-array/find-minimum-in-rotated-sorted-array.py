class Solution(object):
    def findMin(self, nums):
        i,j=0,len(nums)-1
        while i<j:
            mid=(i+j)//2
            if nums[mid]>nums[j]:
                  i=mid+1
            else:
                  j=mid
        return nums[i]


        
        