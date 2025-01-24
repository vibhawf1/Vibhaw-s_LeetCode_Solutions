class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        max_time = 0
        button_index = 0
        prev_time = 0

        for index, time in events:
            # Calculate the push time for the current button
            push_time = time - prev_time 
            
            # Update max_time and button_index if necessary
            if push_time > max_time:
                max_time = push_time
                button_index = index
            elif push_time == max_time and index < button_index:
                button_index = index  # Prioritize smaller index for ties
            
            prev_time = time  # Update prev_time for the next iteration

        return button_index
