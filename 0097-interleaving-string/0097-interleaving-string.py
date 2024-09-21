class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dp(f,s,t):
            if t == len(s3):
                return f == len(s1) and s == len(s2)
            
            fc , sc = False,False
            if f < len(s1) and s3[t] == s1[f]:
                fc = dp(f+1,s,t+1)
            if s < len(s2) and s3[t] == s2[s]:
                sc = dp(f,s+1,t + 1)
            return fc or sc
        return dp(0,0,0)
            
