# Given an array arr[]. The task is to find the largest element and return it.

# Examples:

# Input: arr[] = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.
# Input: arr[] = [5, 5, 5, 5]
# Output: 5
# Explanation: The largest element of the given array is 5.
class Solution:
    def largest(self, arr):
        # code here
        n=len(arr)
        #using the float infinty 
        largest=float("-inf")
        
        for i in range (0,n):
        #an alternative method was also using the max function which is inbuilt but using if else also works the same..
            if arr[i]>largest:
                largest=arr[i]
        return largest
        #hence the loop runs by picking up every single element from the array and checking it with the largest varaiable ..