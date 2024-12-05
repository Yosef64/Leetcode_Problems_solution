class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l , tOr= 0 , 0
        res = 0
        for r in range(len(nums)):
            while l < r and tOr&nums[r] != 0:
                tOr&=~nums[l]
                l += 1
            if tOr & nums[r] == 0:
                res = max(r-l + 1,res)
            tOr |= nums[r]
        return res