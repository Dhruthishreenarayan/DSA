class Solution(object):
    def nextPermutation(self, nums):
       piv=-1
       n=len(nums)
       for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            piv=i
            break
       if piv== -1 :
        nums.reverse()
        return nums
       for i in range(n-1,piv,-1):
        if(nums[i]>nums[piv]):
            nums[i],nums[piv]=nums[piv],nums[i]
            break
       i=piv+1
       j=n-1
       while(i<=j):
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1
       return nums


        