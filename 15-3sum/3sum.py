class Solution(object):
   def threeSum(self, nums):
       result = []
       nums.sort()  # Step 1: Sort the array
       n = len(nums)


       # Step 2: Iterate over each number
       for i in range(n - 2):
           if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
               continue


           target = -nums[i]
           left, right = i + 1, n - 1


           # Step 3: Two-pointer approach
           while left < right:
               sum_val = nums[left] + nums[right]


               if sum_val == target:
                   result.append([nums[i], nums[left], nums[right]])


                   # Step 4: Skip duplicate values
                   while left < right and nums[left] == nums[left + 1]:
                       left += 1
                   while left < right and nums[right] == nums[right - 1]:
                       right -= 1


                   left += 1
                   right -= 1
               elif sum_val < target:
                   left += 1
               else:
                   right -= 1


       return result

       
