class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words , n = sentence.split(" "), len(searchWord)
        for ind,word in enumerate(words):
            if word[:n] == searchWord:
                return ind + 1
        return -1
