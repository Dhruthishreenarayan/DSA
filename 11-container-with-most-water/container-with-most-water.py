class Solution(object):
    def maxArea(self, height):
        n=len(height)
        left=0
        right=n-1
        maxarea=0
        while left<right:
            curheight=min(height[left],height[right])
            curwidth=right-left
            curarea=curheight*curwidth
            maxarea=max(maxarea,curarea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea
        