#brute force app:     #IM TRING TO FIND THE LENGTH THEN LEN ADN AFTER THAT I WILL SUBSTRACT THE N GIVE AND THATS WHERE I REACH MY CURR VARIABLE AND REMOVE IT .
        #TO GET LENGTH
    #optimal now 
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        #taking two points where slow is son of fast as fast takes few advantage and moves n places given in the question where as slow is at the head only 
        
        slow,fast=head,head
        for i in range(n):
            fast=fast.next
        #edge case  - given value of n is same len of the nodes means removing the first node
        if fast==None:
            return head.next
        #checking that fast is at the last pos sot that when slow is behind fast by some distance we know that its time to update the nodes and remove element
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
            #node updation linking
        slow.next=slow.next.next
        return head