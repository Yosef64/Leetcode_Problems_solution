class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans , n = "" , len(s)
        def isGood(ls):
            dic = set(ls)
            for char in ls:
                if char.upper() not in dic or char.lower() not in dic:
                    return False
            return True
        for ind in range(n):
            for ind1 in range(ind + 1,n):
                if isGood(s[ind:ind1+1]) and ind1 - ind + 1 > len(ans):
                    ans = s[ind:ind1+1]
        return ans