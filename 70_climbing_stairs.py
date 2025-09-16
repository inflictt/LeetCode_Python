def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        ways=[1,1,2]#this is the ways to climf for numbers[0,1,2] respectively
        for step in range(3,n+1):#checking for number from 3 to n+1
            ways.append(ways[step-1]+ways[step-2])#basically it looks like the fibonacci sequence or something 
        return ways[n]#returning back the required answer
print(climbStairs(6))