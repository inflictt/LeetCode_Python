class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # i need to return the no of steps 
        colors = "abaac", neededTime = [1,2,3,4,5]
        start=0#starting here
        output = 0 
        # if colors[start]==colors[-1]:
        #     output = neededTime[start]+neededTime[-1]
        n=len(colors)
        for i in range(1,n):
            if colors[start]!=colors[i]:#checking for the 0th and 1st elem 
                start = i #reintitalising
            else:#a==a 
                
                if neededTime[start]>neededTime[i]:#checking if which one is cheap in term of time 
                    output += neededTime[i]
                else :
                    output += neededTime[start]
                    start=i#this is required as we took elem of 

        return output