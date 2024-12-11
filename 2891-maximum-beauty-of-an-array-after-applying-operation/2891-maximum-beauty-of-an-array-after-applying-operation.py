class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,res = 0 , 0
        for r in range(len(nums)):
            while left < r and nums[r] - k > nums[left] + k:
                left += 1
            res = max(res,r - left + 1)
        return res