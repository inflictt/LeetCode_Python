# 1207. Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        #creating an empty dict for storing key values 
        hm = {}
        n = len(arr)
        #iterating and checking and then adding frequencies for the elements in the arr
        for i in range(n):
            hm[arr[i]] = hm.get(arr[i], 0) + 1
        #fetching values and then finally returning over 
        occur = list(hm.values()) 
        #if both are equal that means number of occurences are unique
        return len(occur) == len(set(occur))
    #shorter code version
        # freq = {}
        # for x in arr:
        #     freq[x] = freq.get(x, 0) + 1

        # return len(freq) == len(set(freq.values()))