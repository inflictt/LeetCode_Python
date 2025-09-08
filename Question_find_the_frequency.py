# Given an array arr of positive integers and an integer x. Return the frequency of x in the array.

# Examples :

# Input: arr = [1, 1, 1, 1, 1], x = 1
# Output: 5
# Explanation: Frequency of 1 is 5.
# Input: arr = [1, 2, 3, 3, 2, 1], x=2
# Output: 2
# Explanation: Frequency of 2 is 2.

class Solution:
    def findFrequency(self, arr, x):
        #creating a hash map here help me to properly get the key value pair and return me the required input of my entered number if no then it return 0
        hash_map = {}
        n = len(arr)
        #i have to iterate over my full arr so thats why range (n)
        for i in range(n):
            #now this a crucial step where i am telling my hash map to check for a cretain value that if it in there if yes then reutrn the value and add 1 to else y default it will give 0 and add 1 to it and store it 
            hash_map[arr[i]] = hash_map.get(arr[i], 0) + 1
            #return give the value like the number of the element as in the list basically occurences and if not inside then it throw 0 
        return hash_map.get(x, 0)