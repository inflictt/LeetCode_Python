
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #same as of part 1 till now 
            if slow == fast:#now we wil check where they are meeting and the place they meet we will move the slow at head pos in order to iterate the index pos of the loop
                slow = head#now slow is at head
                while slow != fast:#we willb ve moving the slow and fast one one step only untill they meet and where they meet is the index so yeah answer fetched
                    slow = slow.next
                    fast = fast.next
                return slow
        return None