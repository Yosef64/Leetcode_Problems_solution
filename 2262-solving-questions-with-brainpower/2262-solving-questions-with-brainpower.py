class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)  
        dp = [0] * (n)  
        dp[-1] = questions[-1][0]
        for ind in range(n-2,-1,-1):
            jump = 0
            if questions[ind][1] + ind+1 < n:
                jump = dp[questions[ind][1]+1+ind]
            dp[ind] = max(jump+questions[ind][0],dp[ind+1]) 

        return dp[0]
