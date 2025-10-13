class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # FIX: Handle empty or single-node lists, as no rotation is possible.
        if not head or not head.next:
            return head

        # 1. Find the length and the original tail node.
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        # 2. Find the effective number of rotations (handles k >= length).
        k = k % length
        
        # If effective rotations are 0, the list is unchanged.
        if k == 0:
            return head
        
        # 3. Find the new tail, which is (length - k - 1) steps from the head.
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
            
        # 4. The new head is the node right after the new tail.
        newhead = curr.next
        
        # 5. Cut the list by making the new tail the end.
        curr.next = None
        
        # 6. Connect the original tail to the original head to complete the rotation.
        tail.next = head
        
        return newhead