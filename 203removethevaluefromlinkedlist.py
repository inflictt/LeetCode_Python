# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def removeElements(self, head, val):
#         """
#         :type head: Optional[ListNode]
#         :type val: int
#         :rtype: Optional[ListNode]
        # """
#now create a dummy node to handle edge cases and i want to have created 2 vars so that i can traverse the linked list
def removeElements(self, head, val):
        dummy=ListNode(next=head)
        curr=head
        prev=dummy
        while curr:
            if curr.val==val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.next
        
                