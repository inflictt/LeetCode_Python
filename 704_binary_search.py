class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #this is the basic and required for binary search algorithm nothing much to explain about
        n=len(nums)
        lo,hi=0,n-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                hi=mid-1
            else:
                lo=mid+1
        return -1