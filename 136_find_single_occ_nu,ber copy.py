# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1
nums = [2,2,1]
#using hash map for our brute for method 
hashmap={}
for num in nums:
    hashmap[num]=hashmap.get(num,0)+1#this checks if the  num index value is in the hashmap if yes it updates the value by +1 and if not it set it as by default 0
    
for key in hashmap:
    if hashmap[key]==1:#check for the value of 1 if there we got our single number
        print[key]