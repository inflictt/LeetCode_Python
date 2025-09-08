# Problem Description:

# You are given a non-negative integer n. Your task is to find the sum of the first n natural numbers using recursion. The sum of the first n natural numbers is given by the formula S=1+2+3+...+nS = 1 + 2 + 3 + ... + nS=1+2+3+...+n.



# Input:

# A non-negative integer n, where 0 <= n <= 1000.



# Output:

# An integer representing the sum of the first n natural numbers.



# Example:

# Input: n = 5
# Output: 15  # (1 + 2 + 3 + 4 + 5)
 
# Input: n = 0
# Output: 0   # Sum of zero natural numbers
def sum_of_natural_numbers(n):
    #giving base case is the basic and first part of the recursion ..
    if n==0:
        return 0 
    #the logic im using is that lets take an example where n=4, now to get sum we have to do 4+3+2+1 so we can write this also 4+(3+2+1) which can be written as n+function(n-1)
    return n+sum_of_natural_numbers(n-1)
n=int(input("Enter value of : "))
print("The sum is :",sum_of_natural_numbers(n))