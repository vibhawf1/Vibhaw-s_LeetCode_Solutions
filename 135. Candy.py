def candy(self, ratings: List[int]) -> int:
    n = len(ratings)
    # Initialize an array to track candy distribution
    candies = [1] * n  # Start by giving one candy to each child
    
    # First pass: left to right
    # Ensure children with higher ratings than their left neighbor get more candies
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    
    # Second pass: right to left
    # Ensure children with higher ratings than their right neighbor get more candies
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            # Take the maximum to satisfy both left and right neighbor constraints
            candies[i] = max(candies[i], candies[i+1] + 1)
    
    # Return the total number of candies
    return sum(candies)
