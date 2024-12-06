class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cMax = gMax = nums[0]
        for num in nums[1:]:
            cMax = max(num,cMax+num)
            if cMax > gMax:
                gMax = cMax
        return gMax