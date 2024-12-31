class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (365 + 30)
        for ele in days:
            dp[ele-1] = 1
        pre = -1
        for day in range(days[-1]-1,-1,-1):
            if dp[day]:
                dp[day] = min(dp[day+7]+costs[1],dp[day + 30]+costs[2],dp[day + 1] + costs[0])
                
                pre = dp[day]
            else:
                dp[day] = min(dp[day+7]+costs[1],dp[day + 30]+costs[2]+dp[day + 1] + costs[0],pre)

        return dp[0]
            

