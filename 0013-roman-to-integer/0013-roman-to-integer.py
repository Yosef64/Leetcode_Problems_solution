class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            "C":100,
            "D":500,
            'M':1000
        }
        ans = dic[s[0]]
        
        for i in range(1,len(s)):
            if dic[s[i - 1]] < dic[s[i]]:
                # print(h[s[i-1]])
                ans = ans + dic[s[i]] - (2 * dic[s[i-1]])
            else:
                ans += dic[s[i]]
        return ans
                
        