class Solution:
    def calculateScore(self, s: str) -> int:
        def get_mirror(c):
            return chr((ord('z') - ord('a')) - (ord(c) - ord('a')) + ord('a'))

        character_to_index = dict()
        score = 0
        for i, c in enumerate(s):
            mirror_c = get_mirror(c)
            if mirror_c not in character_to_index or len(character_to_index[mirror_c]) == 0:
                if c not in character_to_index:
                    character_to_index[c] = [i]
                else:
                    character_to_index[c].append(i)
            else:
                closest_index = character_to_index[mirror_c][-1]
                character_to_index[mirror_c].pop(-1)
                score += i - closest_index
        return score
