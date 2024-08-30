class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = []
        for word in words:
            bit = 0
            for char in word:
                num = ord(char) - 97
                
                bit = bit | int( 2 ** ( num ) )
            ans.append(bit)
        # print(ans)
        MaxLength = 0
        for ind in range(len(ans)-1):
            for ind1 in range(ind+1,len(ans)):
                if ans[ind] & ans[ind1] == 0:
                    MaxLength = max(MaxLength,len(words[ind]) * len(words[ind1]))
        return MaxLength