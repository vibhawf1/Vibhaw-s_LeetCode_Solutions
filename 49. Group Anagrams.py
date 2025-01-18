class Solution:
    def areAnagrams(self, word1: str, word2: str) -> bool:
        # Function to check if two words are anagrams
        return sorted(word1) == sorted(word2)

    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        # List to store groups of anagrams
        anagram_groups = []

        # Iterate through each word in the input list
        for word in words:
            # Check if the word is already assigned to an existing group
            assigned = False
            for group in anagram_groups:
                if self.areAnagrams(word, group[0]):
                    group.append(word)
                    assigned = True
                    break
            
            # If the word is not assigned, create a new group
            if not assigned:
                anagram_groups.append([word])

        return anagram_groups
