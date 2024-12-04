class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l , r = 0,0
        while l<len(str1) and r<len(str2):
            
            t = ord(str1[l])+1 if ord(str1[l])!=122 else 97
            if (chr(t)==str2[r]) or str1[l]==str2[r]:
                r+=1
            l+=1
        return r==len(str2)
        