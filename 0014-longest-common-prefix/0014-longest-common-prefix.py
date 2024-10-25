class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        t = [s[0][:x+1] for x in range(len(s[0]))]

        for e in range(1,len(s)):
            c = False
            i = 0
            while i<len(s[e]):
                if len(t)>=i+1 and s[e][:i+1]!=t[i]:
                    c = True
                    break
                i+=1
            t =  t[:i]
            
            if len(t)==0:
                return ""
        return t[-1] if t else ""