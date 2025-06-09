# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            # Store next node
            next_node = current.next
            # Reverse the link
            current.next = prev
            # Move pointers forward
            prev = current
            current = next_node
        
        # prev will be the new head of the reversed list
        return prev
