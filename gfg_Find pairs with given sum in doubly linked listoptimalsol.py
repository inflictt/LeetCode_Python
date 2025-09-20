# # Find pairs with given sum in doubly linked list
# from typing import Optional
# from typing import List

# """

# Definition for singly Link List Node
# class Node:
#     def __init__(self,x):
#         self.data=x
#         self.next=None
#         self.prev=None

# You can also use the following for printing the link list.
# displayList(node)
# # """
# Input:  
# 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
# target = 7
# Output: (1, 6), (2,5)
# Explanation: We can see that there are two pairs 
# (1, 6) and (2,5) with sum 7.

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        #optimal sol
        left=head
        right=head
        res=[]
        while right is not None:
            right=right.next#making right move to end as in order to calc left+right== target if true than we will store data of both in result and then return
        while left is not None and right is not None and left.data<right.data:
            total=left.data+right.data
            if total==target:
                res.append([left.data,right.data])
                left=left.next
                right=right.prev
            elif total>target:
                right=right.prev
            else:
                left=left.next
        return res