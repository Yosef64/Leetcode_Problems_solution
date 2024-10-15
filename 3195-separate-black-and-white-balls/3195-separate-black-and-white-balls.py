class Solution:
    def minimumSteps(self, s: str) -> int:
        ans , s = 0 , list(s)
        black , white = 0 , 1
        while black < white and white < len(s):
            if s[black] == "1" and s[white] == "0":
                ans += white - black
                s[black] , s[white] = s[white],s[black]
            if s[black] == "0":
                black += 1
            
            white+= 1  
        
        return ans
