class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [ind for ind in range(len(s)+1)]
        d = set(dictionary)
        for ind in range(len(s)):
            for i in range(ind,-1,-1):
                if s[i:ind+1] in d:
                    dp[ind+1] = min(dp[ind+1],dp[i])
                else:
                    dp[ind+1] = min(dp[ind+1],ind-i+1+dp[i])
        return dp[-1]


        