class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        from collections import defaultdict
        
        pattern_count = defaultdict(int)
        
        for row in matrix:
            # Create a tuple representing the pattern of the row
            pattern = tuple(row)
            # Create a tuple representing the flipped pattern of the row
            flipped_pattern = tuple(1 - x for x in row)
            # Increment the count for both the pattern and its flipped version
            pattern_count[pattern] += 1
            pattern_count[flipped_pattern] += 1
        
        # The maximum count is the maximum number of rows that can be made equal
        return max(pattern_count.values())
