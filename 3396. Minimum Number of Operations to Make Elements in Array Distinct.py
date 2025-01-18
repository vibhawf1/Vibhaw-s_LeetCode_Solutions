from collections import Counter, defaultdict
class Solution:
    def minimumOperations(self, arr: List[int]) -> int:
        indices = defaultdict(list)

        for i, num in enumerate(arr):
            indices[num].append(i)

        op = 0
        removed = 0

        while True:
            hd = False

            for pos in indices.values():
                valid_indices = 0
                for idx in pos:           
                    if idx >= removed:
                        valid_indices += 1
                        
                if valid_indices > 1:
                    hd=True
                    break
                        
                    
            if not hd:
                break

            removed += 3
            op += 1
        return op
            
        
