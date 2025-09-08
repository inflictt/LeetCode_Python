# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false


class Solution(object):
    def isAnagram(self, s, t):
        #taking the dictionary and then accessing the calue and their occurences in the string and if present then ok but if not then gets added and their occurences increases by 1
        dict1,dict2={},{}
        for item in s:
            dict1[item]=1+dict1.get(dict[item],0)
        for item in t:
            dict2[item]=1+dict2.get(dict[item],0)
        #here it checks and then returns back the required result
        return dict1==dict2
    
check=Solution()
print(check.isAnagram("bat","tab"))