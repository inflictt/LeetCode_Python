def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #creating a max variable to store value of sum where it is maximum
        maxi=float("-inf")
        n=len(nums)
        total=0
        for i in range(0,n):
            #adding value of iteration to total and checking the maximum of total and max and then storing maxi , and if the stored total is negative then it will be given value as 0 as negative number wont help us to get required answer as sum will be sacrifised
            total=total+nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
        return maxi