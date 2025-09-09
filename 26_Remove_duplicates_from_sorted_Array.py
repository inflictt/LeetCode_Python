class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=0
        j=i+1
        while j<n:
            if nums[j]!=nums[i]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1
    #dry run: 
#     Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# here in the output after the unique elems there  they put underscores but we can put anything , 
# so lets take nums[i=0]=1 and putting in the while loop checking conditions nums[j=i+1=1]=1 there both are same , so we increment j+1
#again loop runs now nums[j=2]=2 and hence nums[j]!=nums[i] therefore i+=1 which is the next to 1,1 this 1 will get updated by j=2 hence, after loop end j+1=3, loop condition fails and now we'return i+1