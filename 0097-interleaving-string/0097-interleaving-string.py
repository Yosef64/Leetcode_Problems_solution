class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n , m , tn = len(s1),len(s2),len(s3)
        @cache
        def dp(f,s,t):
            if t == tn:
                return f == n and s == m
            
            fc , sc = False,False
            if f < n and s3[t] == s1[f]:
                fc = dp(f+1,s,t+1)
            if s < m and s3[t] == s2[s]:
                sc = dp(f,s+1,t + 1)
            return fc or sc
        return dp(0,0,0)
            
