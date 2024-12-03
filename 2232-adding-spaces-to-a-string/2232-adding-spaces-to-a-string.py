class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = [s[:spaces[0]]]
        for ind in range(1,len(spaces)):
            words.append(s[spaces[ind-1]:spaces[ind]])
        words.append(s[spaces[-1]:])
        
        return " ".join(words)