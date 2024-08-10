class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        dic = defaultdict(list)
        memo = {}
        for ind,char in enumerate(t2):
            dic[char].append(ind)
        
        def dp(f,s):
            if f == len(t1) or s == len(t2):
                return 0
            if (f,s) not in memo:
                include = 0
                for ind in dic[t1[f]]:
                    if ind >= s:
                        include = dp(f + 1, ind+1) + 1
                        break
                exclude = dp(f + 1, s)
                memo[(f,s)] = max(include,exclude)
            return memo[(f,s)]
        return dp(0,0)