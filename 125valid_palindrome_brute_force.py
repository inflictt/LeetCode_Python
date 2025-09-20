class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstr=""#extra variable or space to store the updated string
        for c in s:
            if c.isalnum():#takes only alphanumberic character only 
                newstr+=c.lower()#removes the issue of a letter being capital and other lowercase
        return newstr==newstr[::-1]#check with the reversed of the string tfor palindrome