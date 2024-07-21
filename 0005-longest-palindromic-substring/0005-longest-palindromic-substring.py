class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi=""
        i=0
        j=len(s)-1
        while i<=j:
            m = s[i:j+1][::-1]
            if s[i:j+1]==m:
                if len(s[i:j+1])>len(maxi):
                    maxi=s[i:j+1]
                i+=1
                j=len(s)-1
            elif s[i:j+1]!=m and i==j-1:
                i+=1
                j=len(s)-1
            else:
                j-=1
        return maxi
        