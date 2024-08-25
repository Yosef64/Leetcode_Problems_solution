class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def comb(cur):
            if cur <= 0:
                return cur == 0
            if cur in memo:return memo[cur]
            ans = 0
            for ele in nums:
                ans += comb(cur-ele)
            return ans
        
        for num in range(1,target+1):
            memo[num] = comb(num)
        return memo[target]
        