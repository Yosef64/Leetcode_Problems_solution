class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n , m = len(s) , len(t)
        @cache
        def dp(fInd,sInd):
            if fInd == n or sInd == m:
                # print(fInd,sInd)
                return int(sInd == m)
            if s[fInd] == t[sInd]:
                return dp(fInd+1,sInd+1) + dp(fInd+1,sInd)
            return dp(fInd+1,sInd)
        return dp(0,0)
        