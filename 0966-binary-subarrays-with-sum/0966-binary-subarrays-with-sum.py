class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        presum , n = [nums[0]], len(nums)
        for ind in range(1,n):
            presum.append(presum[-1]+nums[ind])
        
        dic ,res = defaultdict(int), 0
        l = 0
        for r in range(n):
            if (presum[r] == goal and presum[r] + presum[l] == goal) and (presum[r]!=0 or presum[l] !=0):
                dic[presum[r]] += 1
            while l < r and presum[r]-presum[l] >= goal:
                
                if presum[r] - presum[l] == goal:
                    dic[presum[r]] += 1
                l += 1
            if presum[r] == goal and not dic[presum[r]]:dic[presum[r]] += 1
            res += dic[presum[r]]
        return res
        