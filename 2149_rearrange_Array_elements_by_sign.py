# 2149. Rearrange Array Elements by Sign

# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

# Example 1:

# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
nums = [3,1,-2,-5,2,-4]
l1,l2,res=[],[],[] #made 3 list one for saving all +no. one for all-ve num and res = result list
n=len(nums)

for i in range(0,n):
    if nums[i]>0:
        l1.append(nums[i])#store all +ves
    else:
        l2.append(nums[i])#stores all -ves
#here the loop adds all the number from l1 and l2 alternately in order to get our final output
for i in range(len(l1)):
    res.append(l1[i])  
    res.append(l2[i])