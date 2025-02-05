class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If the strings are already equal, return True
        if s1 == s2:
            return True
        
        # Find the indices where the characters differ
        diff_indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)
        
        # If there are more than two differing indices, return False
        if len(diff_indices) != 2:
            return False
        
        # Check if swapping the characters at the differing indices makes the strings equal
        i, j = diff_indices
        return s1[i] == s2[j] and s1[j] == s2[i]
