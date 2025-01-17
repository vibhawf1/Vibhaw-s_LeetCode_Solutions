class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        if not digits:
            return answer
        digit_to_letter = {"2" : "abc",
                           "3" : "def",
                           "4" : "ghi",
                           "5" : "jkl",
                           "6" : "mno",
                           "7" : "pqrs",
                           "8" : "tuv",
                           "9" : "wxyz"}
        curr = []

        def dfs(idx):
            if idx == len(digits):
                answer.append("".join(curr))
                return
            for letter in digit_to_letter[digits[idx]]:
                curr.append(letter)
                dfs(idx+1)
                curr.pop()
        
        dfs(0)
        return answer
