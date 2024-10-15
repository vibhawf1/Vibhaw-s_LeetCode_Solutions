class Solution:
    def minimumSteps(self, s: str) -> int:
        ones_positions = []  # Stores the indices of all '1's
        
        # Collect the positions of all '1's
        for i, char in enumerate(s):
            if char == '1':
                ones_positions.append(i)
        
        # Calculate minimum swaps
        min_steps = 0
        total_ones = len(ones_positions)
        
        # For each '1', calculate how many steps it needs to move to its target
        for i, pos in enumerate(ones_positions):
            target_position = len(s) - total_ones + i  # The target position for this '1'
            min_steps += target_position - pos  # Count how many swaps are needed
        
        return min_steps
