class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        #here lowerbound=n as in order to give the appended index position to number not present in the list by default
        lb=n
        #start and end of the arr
        lo,hi=0,n-1
        while lo<=hi:#base condition as they must not overlap
            mid=(lo+hi)//2#to get the mid so we can calculate out further queries
            if nums[mid]>=target:#checking this to get the least index possible 
                lb=mid
                hi = mid-1
            else:
                lo=mid+1
        return lb
