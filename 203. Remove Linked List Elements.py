# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize pointers
        current = dummy
        
        # Traverse the list
        while current.next:
            # If the next node has the target value, remove it
            if current.next.val == val:
                current.next = current.next.next
            # Otherwise, move to the next node
            else:
                current = current.next
        
        # Return the new head
        return dummy.next
