class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans , l = 0 , 0
        for ind in range(3,len(nums)+1):
            if not nums[l]:
                ans += 1
                for i in range(l,l+3):
                    nums[i] = not nums[i]
            l += 1
        # print(nums,ans)
        return ans if all(nums) else -1