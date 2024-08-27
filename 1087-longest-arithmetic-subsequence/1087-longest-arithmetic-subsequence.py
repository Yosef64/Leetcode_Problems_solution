class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp , ans = defaultdict(int) , 0

        for ind , val in enumerate(nums):
            for j in range(ind):
                dif = val - nums[j]
                if dp[(j,dif)]:
                    dp[(ind,dif)] = max(dp[(ind,dif)],dp[(j,dif)]+1)
                else:
                    dp[(ind,dif)] =  max(dp[(ind,dif)],1)
                ans = max(ans,dp[(ind,dif)])
        return ans + 1
        


                
        ans = 0
        for key in dic:
            ans = max(ans,dic[key])
        return ans + 1