# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
class Solution(object):
    def groupAnagrams(self, strs):
        res={}
        for s in strs:
            #did this in order to create a hashmap for my value and their occurences part taking all as zero in the start and updating their values in later part 
            count=[0]*26
            for c in s:
                #doing -ord"a" as in order to map the values of the haslist like in given question we have only small char so thats why .. and then incrementing to update their values as of occurences
                count[ord(c)-ord("a")]+=1
            key=tuple(count)
            #this line changes the mutable list into an unchangeable tuple
            if key not in res:
                res[key]=[s]
            else:
                res[key].append(s)
        return list(res.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
check=Solution()
print("ans is : ",check.groupAnagrams(strs))