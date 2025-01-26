class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        j = 0  # Index for spaces array
        i = 0  # Index for string s
        
        while i < len(s):
            if j < len(spaces) and i == spaces[j]:
                result.append(" ")  # Add space
                j += 1
            result.append(s[i])  # Add character from s
            i += 1
        
        return "".join(result)
