class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        first=''.join(sorted(s))
        second=''.join(sorted(t))
        if first==second:
            return True
        else:
            return False