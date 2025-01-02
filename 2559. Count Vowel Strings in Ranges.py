class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix = [0]

        count = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            prefix.append(count)

        result = []
        for left, right in queries:
            result.append(prefix[right + 1] - prefix[left])
        return result
