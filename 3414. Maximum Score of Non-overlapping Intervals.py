class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted((*interval, idx) for idx, interval in enumerate(intervals))
        
        @cache
        def rec(candidate_idx, intervals_remaining) -> Tuple[int, Tuple[int]]:
            if candidate_idx == len(intervals):
                return 0, ()
            
            weight_if_not_taken, selection_if_not_taken = rec(candidate_idx + 1, intervals_remaining)
            result_weight, result_selection = weight_if_not_taken, selection_if_not_taken
            
            if intervals_remaining:
                next_candidate_idx = bisect.bisect_right(intervals, (intervals[candidate_idx][1], float('inf')))
                
                weight_if_taken, selection_if_taken = rec(next_candidate_idx, intervals_remaining - 1)
                weight_if_taken += intervals[candidate_idx][2]
                selection_if_taken = (intervals[candidate_idx][3], *selection_if_taken)
                
                if weight_if_taken > weight_if_not_taken or (weight_if_taken == weight_if_not_taken and selection_if_taken < selection_if_not_taken):
                    result_weight, result_selection = weight_if_taken, selection_if_taken
                    
            return result_weight, result_selection    
            
        _, interval_selection = rec(0, 4)
        return sorted(list(interval_selection))
