# Find pairs with given sum in doubly linked list
from typing import Optional
from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
# """
# Input:  
# 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
# target = 7
# Output: (1, 6), (2,5)
# Explanation: We can see that there are two pairs 
# (1, 6) and (2,5) with sum 7.

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        #better sol
        myset=set()
        temp=head
        res=[]
        while temp is not None:
            rem=target-temp.val
            if rem in myset:
                res.append([rem,temp.val])
            myset.add(temp.val)
            temp=temp.next
        return res