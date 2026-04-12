class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        left,right=0,m
        while left <= right:
            i=(left+right)//2
            j=(m+n+1)//2-i
            maxlef1=float('-inf') if i==0 else nums1[i-1]
            minrig1=float('inf') if i==m else nums1[i]
            maxlef2=float('-inf') if j==0 else nums2[j-1]
            minrig2=float('inf') if j==n else nums2[j]
            if maxlef1 <= minrig2 and maxlef2 <= minrig1:
                if (m+n)%2==0:
                    return (max(maxlef1,maxlef2)+min(minrig1,minrig2))/2.0
                else:
                    return max(maxlef1,maxlef2)
            elif maxlef1 > minrig2:
                right=i-1
            else:
                left=i+1



        