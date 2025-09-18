class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #initiallising two var as slow and fast as slow move once and fast move twice as of slow 
        slow,fast=head , head
        #condition is for the out of bound problem
        while (fast is not None) and (fast.next is not None):
            slow=slow.next#move one position
            fast=fast.next.next#moves two positions
            if slow==fast:#and if they are meeting at any point we are required to return true
                return True
        return False#else false if they never met
    