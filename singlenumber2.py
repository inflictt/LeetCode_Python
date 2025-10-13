class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # using hashmap
        hs={}#to get number and updating its occurence
        for num in nums :#itr over full list
            hs[num]=hs.get(num,0)+1#getting the value if not there and adding up its occurences if there already
        for number,occurrences in hs.items():#itr the hashmap created 
            if occurrences==1:#our required case of a  single number item
                return number
        return -1