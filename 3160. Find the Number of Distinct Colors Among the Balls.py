from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Dictionary to store the color of each ball
        ball_colors = {}
        # Dictionary to store the count of each color
        color_counts = {}
        # List to store the result after each query
        result = []
        
        for x, y in queries:
            # If the ball already has a color, decrement the count of that color
            if x in ball_colors:
                old_color = ball_colors[x]
                color_counts[old_color] -= 1
                if color_counts[old_color] == 0:
                    del color_counts[old_color]
            
            # Update the ball's color
            ball_colors[x] = y
            
            # Increment the count of the new color
            if y in color_counts:
                color_counts[y] += 1
            else:
                color_counts[y] = 1
            
            # Append the number of distinct colors to the result
            result.append(len(color_counts))
        
        return result
