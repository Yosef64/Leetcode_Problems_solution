class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dic , ans = {x:0 for x in nums}, 0
        def fn(num):
            
            if num not in dic or dic[num]:
                return 0 if num not in dic else dic[num]
            s = fn(num** 2) + 1
            dic[num] = s
            return dic[num]
        
        for num in nums:
            if not dic[num]:
                s = fn(num ** 2) + 1
                ans = max(ans,s)
        return ans if ans != 1 else -1
        

        