class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memoMap = {}
        
        def lcs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            key = (i, j)
            if key in memoMap:
                return memoMap[key]
            if text1[i] == text2[j]:
                result = 1 + lcs(i + 1, j + 1)
            else:
                result = max(lcs(i, j + 1), lcs(i + 1, j))
            memoMap[key] = result
            return result
        
        return lcs(0, 0)