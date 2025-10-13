# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7.
head = [4,2,2,3]
  # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        #using tort and hare technique to get the mid and then after getting mid and then reverse first half of it so when we will move form in to out we will sum and check things for our answers
        slow,fast=head,head
        prev=None
        while fast and fast.next :
            fast=fast.next.next
            tmp=slow.next#usnig to move slow ptr further 
            slow.next=prev#helps in reversing
            prev=slow#storing slow as it get updated
            slow=tmp#tmp is nothing othr than slow.next
        res=0#our answer
        while slow:#can be prev also or slow as even iteration
            res=max(res,prev.val+slow.val)#inbuilt max funciton for getting the maximum value only
            prev=prev.next
            slow=slow.next
        return res