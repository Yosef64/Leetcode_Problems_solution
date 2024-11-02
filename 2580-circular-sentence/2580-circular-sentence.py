class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[-1] != sentence[0]:return False

        words = sentence.split(" ")
        for ind in range(len(words)-1):
            if words[ind][-1] != words[ind+1][0]:
                return False
        return True