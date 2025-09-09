def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
        return nums
nums=[3,9,5,6,7,2,10,9]
n=len(nums)
k=5
reverse(nums,n-k,n-1) #this is for the last k elements
reverse(nums,0,n-k-1) #this if for the remaining elements

print(reverse(nums,0,n-1)) #final reverse of the full array 