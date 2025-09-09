def check_array(nums):
    n=len(nums)
    for i in range (0,n-1):
        #to check if the given is sorted we check two adjacent elements and if they are sorted we'll pick up next adjacent pair and check if they are sorted 
        if nums[i]>nums[i+1]:
            #if they are not sorted then we'll return false
            return False
        #if everything is perfect we'll return True
    return True
nums=[1,2,3,4,5,6,7]
print("the given nums array is sorted : ", check_array(nums))