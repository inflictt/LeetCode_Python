# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7.
head = [4,2,2,3]
class Solution(object):
    def pairSum(self, head):
        start=head
        lst=[]
        while start:
            lst.append(start.val)
            start=start.next
        return lst

check=Solution(head)
print(check)