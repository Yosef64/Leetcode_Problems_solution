class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum , minEle = nums[0] , nums[0]
        ans = nums[0]
        for num in nums[1:]:
            presum += num
            ans = max(ans,presum,presum - minEle,presum - num)
            minEle = min(minEle,presum)
        return ans 