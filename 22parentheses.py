class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []  # A list to store our final answers.
        
        # This function will build the parenthesis strings.
        # 'current' is the string we are building.
        # 'open_count' and 'close_count' count the number of '(' and ')' brackets.
        def solve(current, open_count, close_count):
            
            # We stop when open_count and close_count are both equal to n.
            # This means the string is complete and is a proper fit.
            if open_count == n and close_count == n:
                result.append(current)
                return

            # If the number of open brackets is less than n, we can add another '('.
            if open_count < n:
                solve(current + "(", open_count + 1, close_count)

            # We can add a ')' only if there are more open brackets than closed ones.
            # This makes sure the brackets stay in the correct order.
            if close_count < open_count:
                solve(current + ")", open_count, close_count + 1)
        
        # Start the function with an empty string and counts at 0.
        solve("", 0, 0)
        
        return result