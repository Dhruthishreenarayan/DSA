class Solution(object):
    def findThePrefixCommonArray(self, A, B):
      n=len(A)
      res=[]
      setA=set()
      setB=set()
      common=0
      for i in range(n):
        setA.add(A[i])
        setB.add(B[i])
        common=len(setA & setB)
        res.append(common)
      return res
