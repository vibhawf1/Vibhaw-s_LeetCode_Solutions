class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_events, y_events = [], []

        for x, y, xx, yy in rectangles:
            x_events.append((x, 1)) 
            x_events.append((xx, -1))
            y_events.append((y, 1))   
            y_events.append((yy, -1)) 

        x_events.sort()
        y_events.sort()

        if self.valid_cuts(x_events, n):
            return True
            
        if self.valid_cuts(y_events, n):
            return True

        return False

    def valid_cuts(self, events, n):
        pre_sum = 0
        count = 0

        for coord, delta in events:
            pre_sum += delta
            if pre_sum == 0:
                count += 1
                if count >= 3:
                    return True
        
        return False
