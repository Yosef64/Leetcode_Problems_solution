class Solution:
    def makeFancyString(self, s: str) -> str:
        ls = []
        for char in s:
            if not ls or ls[-1][0] != char:
                ls.append([char,1])
            
            elif ls and ls[-1][1] < 2:
                ls[-1][1] += 1
        ans = ""
        for char , occ in ls:
            ans += char * occ
        return ans
        