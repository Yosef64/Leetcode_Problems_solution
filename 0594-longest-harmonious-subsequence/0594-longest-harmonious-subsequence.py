class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count , ans = Counter(nums), 0
        for num in count:
            if count[num+1] > 0:
                ans = max(ans,count[num] + count[num+1])
        return ans