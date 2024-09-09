# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        matrix = [ [-1] * n for _ in range(m) ]
        curr = head
        #             right.    down.   left.     up.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_pointer = 0

        r, c = 0, 0

        while curr:
            matrix[r][c] = curr.val
            curr = curr.next

            # Compute next position
            dr, dc = directions[direction_pointer]
            next_r, next_c = r + dr, c + dc
            
            # Check if the next position is within bounds and unfilled
            if not (0 <= next_r < m and 0 <= next_c < n and matrix[next_r][next_c] == -1):
                direction_pointer = (direction_pointer + 1) % 4
                dr, dc = directions[direction_pointer]
                next_r, next_c = r + dr, c + dc
            
            # Update the current position
            r, c = next_r, next_c
        
        return matrix

