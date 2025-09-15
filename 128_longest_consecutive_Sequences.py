# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # create a set as in order to remove the repeated elements if any as they are of no use to us in this required question
    num_Set = set(nums)
    longest = 0
    # longest is the required the length asked in the question to us
    for num in num_Set:  # iterating numSet
        # here we know if we dont have a num-1 element in the set then num is our starting element
        if num - 1 not in num_Set:
            length = 1
            # we have to check the series so for that we will be again and again iterating tis loop until our sequence breaks
            while (num + length) in num_Set:
                length += 1
            if length > longest:
                longest = length
    return longest


nums = [100, 4, 200, 1, 3, 2]
ans = longestConsecutive(nums)
print(ans)
