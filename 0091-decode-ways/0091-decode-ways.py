class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(cur,ind):
            if cur=="0":return 0
            if cur and int(cur) > 26 or ind >= len(s):
                return int(int(cur) <= 26)
            if s[ind]=="0":return dp(cur+s[ind],ind+1)
            return dp(cur+s[ind],ind+1) + dp(s[ind],ind+1)
        return dp(s[0],1)
    

        