# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        # Initialize slow and fast pointers
        slow = head
        fast = head
        
        # Move slow by 1 step and fast by 2 steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If slow and fast meet, there's a cycle
            if slow == fast:
                return True
        
        # If we reach here, fast has reached the end, so no cycle
        return False
