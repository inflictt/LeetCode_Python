# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: n
# Output: 4
nums = [4,5,6,7,0,1,2]
target = 0
n=len(nums)

def search(self, nums, target):
    lo=0
    hi=n-1
    while lo<=hi:
        mid=(lo+hi)//2
        #returning if the element is meeting the requried condition in the question
        if nums[mid]==target:
            return mid
        #checking if the right part is sorted or not from the mid element
        if nums[mid]<=nums[hi]:
            #checking if the target lies between them or not
            if nums[mid]<=target<=nums[hi]:
                lo=mid+1
            else:
                    hi=mid-1
        else:
            #checking if the left part from the mid element is sorted or not
            if nums[mid]>=target>nums[lo]:
                hi=mid-1
            else:
                lo=mid+1
    return -1