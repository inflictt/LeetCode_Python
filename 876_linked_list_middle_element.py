class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n = 0# count the number of  elemnts in the node
        temp = head#startss at the first position
        while temp is not None:#checks to find the last element
            n += 1
            temp = temp.next#move on to one to another in a sequence
        temp = head#reinitialised at start position
        for i in range(0, n // 2):#move upto the middle of the length pass the positon to the temp and then it return back
            temp = temp.next
        return temp
