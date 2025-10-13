# Input: nums = [2,7,11,15], target = 9
nums = [2,7,11,15]
target = 9
i,j=0,1
n=len(nums)
while j<=n:
    sum=nums[i]+nums[j]
    if sum==target: