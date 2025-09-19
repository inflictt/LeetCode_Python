class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        len=0
        temp=head
        slow,fast=head , head
        while (fast is not None) and (fast.next is not None):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                len=1
                while slow!=fast:
                    slow=slow.next
                    len+=1
                return len
        return 0
        