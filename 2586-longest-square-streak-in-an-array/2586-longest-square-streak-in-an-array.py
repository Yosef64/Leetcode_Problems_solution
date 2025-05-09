class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dic , ans = {x:0 for x in nums}, 0
        def fn(num):
            if num not in dic:
                return 0
            if dic[num]:
                return dic[num]
            return fn(num**2) + 1
        
        for num in nums:
            if not dic[num]:
                s = fn(num ** 2) + 1
                ans = max(ans,s)
        return ans if ans != 1 else -1
        

        