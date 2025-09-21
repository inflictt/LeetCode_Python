# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1
nums = [2,2,1]
#optimal sol using xor opr method 
#as a^a=0 using this formula we will get out single occurence number from the arr
ans=0
def check(nums,ans):
    for i in nums:
        ans=ans^i#taking xor with each value present inside the arr so that in the end we get our required ans
    return ans
print(check(nums,ans))