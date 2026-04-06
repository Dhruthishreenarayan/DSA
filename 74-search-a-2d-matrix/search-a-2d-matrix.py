class Solution(object):
    def searchMatrix(self, matrix, target):
       if not matrix or not matrix[0]:
         return False
       m=len(matrix)
       n=len(matrix[0])
       sr=0
       er=n*m-1
       while sr <=  er:
         mid=(sr+er)//2
         r=mid//n     
         c=mid%n
         if matrix[r][c]==target:
            return True
         elif matrix[r][c] < target :
            sr=mid+1
         else:
            er=mid-1
       return False
        