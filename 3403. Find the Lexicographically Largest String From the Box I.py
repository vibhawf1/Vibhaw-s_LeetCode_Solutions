class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        lr_pair = ["a", []]
        for i in range(len(word)):
            if ord(word[i]) > ord(lr_pair[0]):
                lr_pair = [word[i], [i]]
            elif word[i] == lr_pair[0]:
                lr_pair[1].append(i)

        if len(word) == numFriends:
            return lr_pair[0]

        optimumFriends = len(word)
        maxLen = optimumFriends - (numFriends-1)
        res = word[lr_pair[1][0]: lr_pair[1][0]+maxLen]
        for lens in lr_pair[1]:
            res = max(word[lens: lens+maxLen], res)
        return res    
        
