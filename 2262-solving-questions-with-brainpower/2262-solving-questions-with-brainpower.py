class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)  
        dp = [0] * (n)  
        dp[-1] = questions[-1][0]
        for ind in range(n-2,-1,-1):
            jump = float("-inf")
            con = questions[ind][1] + ind+1 < n
            if con:
                jump = dp[questions[ind][1]+1+ind]
                # print(jump,questions[ind][0])
            dp[ind] = max(jump+questions[ind][0],dp[ind+1]) if con else max(questions[ind][0],dp[ind+1])
            # print(ind,dp,max(jump+questions[ind][0],dp[ind-1]))
        return dp[0]
            

        return dp[time_limit] 