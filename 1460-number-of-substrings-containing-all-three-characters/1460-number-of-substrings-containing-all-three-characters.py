class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = {}
        l , ans = 0, 0
        for r in range(len(s)):
            dic[s[r]] = dic[s[r]] + 1 if s[r] in dic else 1
            while len(dic) == 3 and dic[s[l]] > 1:
                
                dic[s[l]] -= 1
                l += 1
            if len(dic) == 3:
                ans += l + 1
        return ans

