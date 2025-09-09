class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #here we will take the length 
        n = len(nums)
        #checking this will help us not to get out of our indexs
        k = k%n
        #we have to do that in place so by slicing method we'solve this question
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums
rotate=Solution()
nums = [1,2,3,4,5,6,7]
k = 3
rotate.rotate(nums,k)
print("The rotate array is : ",nums)