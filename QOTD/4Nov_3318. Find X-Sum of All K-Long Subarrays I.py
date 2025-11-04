class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)#it is the len of nums
        ans = []  #ans later gets elem appended in it
        for i in range(0,n-k+1):#goes upto to n-k+1 as the requirement by ques for subarray
            li=nums[i:i+k]#making the list gets all the elements upto i+k eg, 
            li.sort(reverse=True)#make the list sorted and get settle in the reverse order so later we have to pick element coming for single time and then picking will be done on the basis of the number not the occurecne like 2:3time,4:1time,3:1time so 4 will be picked as the largest num
            dict=Counter(li)#creates a coutner dict like counter collection
            b=sorted(dict,key=dict.get,reverse=True)#sorts the dict 
            sum=0#sum gets reinitiallised every time loop runs
            for i in range(x):#moves only upto x times
                if i >=len(b):#checks for the i > len (b)
                    break
                sum+=dict[b[i]]*b[i]#sum += (frequency * number) it is written like this 
            ans.append(sum)
        return ans