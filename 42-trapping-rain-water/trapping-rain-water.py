class Solution(object):
    def trap(self, height):
       n=len(height)
       ans=0
       lmax,rmax=height[0],height[n-1]
       low,high=1,n-2
       while low<=high:
         lmax=max(lmax,height[low])
         rmax=max(rmax,height[high])
         if lmax<rmax:
            ans+=lmax-height[low]
            low+=1
         else:
            ans+=rmax-height[high]
            high-=1
       return ans