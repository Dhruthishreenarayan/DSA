class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        next_gen={}
        for num in nums2:
            while stack and num > stack[-1]:
                smaller=stack.pop()
                next_gen[smaller]=num
            stack.append(num)
        while stack:
            next_gen[stack.pop()]=-1
        return [next_gen[num] for num in nums1]

        