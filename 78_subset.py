# 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums = [1,2,3]
powset=[[]]
n=len(nums)
for i in range (n):
    powset.append([i])
    for j in range (1,n):
        add=[nums[i],nums[j]]
        powset.append(add)
            
        
powset.append(nums)
print(powset)