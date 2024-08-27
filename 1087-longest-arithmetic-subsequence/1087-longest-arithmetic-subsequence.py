class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp , ans = [] , 0

        for ind , val in enumerate(nums):
            temp = defaultdict(int)
            for j in range(ind):
                dif = val - nums[j]
                if dif in dp[j]:
                    temp[dif] = max(temp[dif],dp[j][dif]+1)
                else:
                    temp[dif] =  max(temp[dif],1)
                ans = max(ans,temp[dif])
            dp.append(temp)
        return ans + 1
        


                
        ans = 0
        for key in dic:
            ans = max(ans,dic[key])
        return ans + 1