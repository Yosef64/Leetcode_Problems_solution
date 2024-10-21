class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        v , n = set() , len(s)
        ans = 0
        def rec(ind,path):
            nonlocal ans
            if ind == n:
                ans = max(ans,len(path))
                return ans
            newS = ""
            for i in range(ind,n):
                newS += s[i]
                if newS not in path:
                    rec(i+1,path.union({newS}))

            return ans
        
        return rec(0,set())
    
    
            