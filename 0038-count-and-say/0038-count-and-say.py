class Solution:
    def count(self,s):
        c , res = 1 , ""
        for ind in range(1,len(s)):
            if s[ind] != s[ind-1]:
                res += str(c) + s[ind-1]
                c = 1
            else:
                c += 1
        res += str(c) + s[-1]
        return res
    def countAndSay(self, n: int) -> str:
        
    
        def rec(cur,s):
            if cur == n:
                return s
            return rec(cur+1,self.count(s))
        return rec(1,"1")



        