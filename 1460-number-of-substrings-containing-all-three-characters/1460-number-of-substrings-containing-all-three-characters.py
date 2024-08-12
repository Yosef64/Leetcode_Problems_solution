class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans , l = 0 , 0
        win = {}
        for r in range(len(s)):
            
            win[s[r]] = win[s[r]] + 1 if s[r] in win else 1
            while len(win) == 3 and win[s[l]] > 1:
                win[s[l]] -= 1
                l += 1
            if len(win) == 3:
                # print(l,r)
                ans += l+1 
        return ans

