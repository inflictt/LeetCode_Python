class Solution:
    def oddEvenList(self, head):
        #checking the edge case for the question
        if not head or not head.next:
            return head
        #using these two points help us to iterate the required indexs
        odd, even = head, head.next
        even_head = even
        #running this loop until its out of nodes
        while even and even.next:
            odd.next = even.next#so the odd indexs are the one which are next to even indexs
            odd = odd.next
            even.next = even.next.next
            even = even.next
        #joining the end of the odd node to even node start
        odd.next = even_head  
        return head