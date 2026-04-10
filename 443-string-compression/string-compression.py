class Solution(object):
    def compress(self, chars):
       write=0      #creates new chars array
       i=0
       while i < len(chars):
         char=chars[i]
         count=0         #count of character
         while i<len(chars) and chars[i]==char:
            i+=1        
            count+=1
         chars[write]=char
         write+=1
         if count >1:
            for c in str(count):    #str(count)=>converts int to str
                chars[write] = c
                write+=1
       return write
       