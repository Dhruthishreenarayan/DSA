class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
       prefix=set()
       for num in arr1:
        while num>0:
            prefix.add(num)
            num//=10
       ans=0
       for num in arr2:
        while num>0:
            if num in prefix:
                ans=max(ans,len(str(num)))
            num//=10
       return ans

         

        