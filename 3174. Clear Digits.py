class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                if stack:  # Make sure the stack is not empty
                    stack.pop()  # Remove the closest non-digit to the left
            else:
                stack.append(char)
        return ''.join(stack) 
