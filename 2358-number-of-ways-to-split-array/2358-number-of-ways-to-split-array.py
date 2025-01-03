class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total ,res = sum(nums), 0
        l = 0
        for num in nums[:-1]:
            total -= num
            l += num
           
            if l >= total:
                res += 1
        return res
