# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        # Edge case: If there's only one node, return the list as it is.
        if not head or not head.next:
            return head
        
        current = head
        
        while current and current.next:
            # Calculate GCD of current node and next node's values
            gcd_value = math.gcd(current.val, current.next.val)
            
            # Create a new node with the GCD value
            gcd_node = ListNode(val=gcd_value)
            
            # Insert the GCD node between current and next
            gcd_node.next = current.next
            current.next = gcd_node
            
            # Move to the node after the newly inserted GCD node
            current = gcd_node.next
        
        return head
