class Solution(object):
    def isPalindrome(self, s):
       n=len(s)
       low,high=0,n-1
       while low < high:
        if not s[low].isalnum():
            low+=1
        elif not s[high].isalnum():
            high-=1
        elif s[low].lower()==s[high].lower():
            low+=1
            high-=1
        else:
            return False
       return True
        