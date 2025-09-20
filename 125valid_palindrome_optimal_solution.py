class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:#checks for out of condition
            while left < right and not self.isalphanumeric(s[left]):#checks for out of condition and if the char is alphanum or not 
                left += 1
            while left < right and not self.isalphanumeric(s[right]):#checks for out of condition and if the cahr is alpha num or not
                right -= 1
            #checks if the string on the both points are equal or not if not than return false
            if s[left].lower() != s[right].lower():
                return False

            left, right = left + 1, right - 1
        #hence after the full opeartion we will get our required output
        return True

    def isalphanumeric(self, c):#returns only the alpha num 
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


s = "A man, a plan, a canal: Panama"
check = Solution()
print(check.isPalindrome(s))
