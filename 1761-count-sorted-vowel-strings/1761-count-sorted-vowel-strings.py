class Solution:
    def countVowelStrings(self, n: int) -> int:
        memo = {}
        def dp(ind,cur):
            if ind == 4:return 1

            if (ind,n) in memo:return memo[(ind,n)]
            curAns = 1
            for com in range(1,cur):
                for i in range(ind+1,5):
                    # print(i,com)
                    curAns += dp(i,com)
            
            memo[(ind,cur)] = curAns
            return memo[(ind,cur)]
        ans = 0
        for i in range(5):
            ans += dp(i,n)
        return ans
