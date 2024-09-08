class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Count the total number of nodes
        total_length = 0
        temp = head
        while temp:
            total_length += 1
            temp = temp.next
        
        # Determine the base size of each part and the number of parts that will get an extra node
        base_size = total_length // k
        extra_nodes = total_length % k
        
        ans = []
        current = head
        
        for i in range(k):
            part_size = base_size + (1 if i < extra_nodes else 0)
            part_head = current
            
            # Split the part
            for j in range(part_size - 1):
                if current:
                    current = current.next
            
            # Disconnect the current part from the rest of the list
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            ans.append(part_head)
        
        return ans
