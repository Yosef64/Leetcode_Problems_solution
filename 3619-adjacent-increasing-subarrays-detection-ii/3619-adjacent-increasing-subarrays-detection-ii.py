class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ls ,res = [], 1
        count = 1
        for ind in range(len(nums)-1):
            if nums[ind] < nums[ind+1]:
                count += 1
            else:
                res = max(min(count,ls[-1]),count//2,res) if ls else max(count//2,res)
                # print(res)
                ls.append(count)
                count = 1
        res = max(min(count,ls[-1]),count//2,res) if ls else max(count//2,res)
        return res

