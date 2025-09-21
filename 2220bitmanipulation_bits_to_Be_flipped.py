# 2220. Minimum Bit Flips to Convert Number
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

# For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
# Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

 

# Example 1:

# Input: start = 10, goal = 7
# Output: 3
start = 10
goal = 7
count=0
check=start^goal#using the xor method as in xor if the number of 1s are even then it gives 0 and number of 1s are odd its gives 1 as output so in order to count the bits flipped we have used xor
for i in range(32):
    if check&(1<<i)!=0:#using check and 1leftshift i that means it will check every bit upto 31st bit and add up number of in output to our count and gives us count as our required output
        count+=1
print(count)