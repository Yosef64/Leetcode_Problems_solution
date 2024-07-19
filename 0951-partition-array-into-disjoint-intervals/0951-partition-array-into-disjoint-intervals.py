class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxEles , maxEle = [] , 0
        for ele in nums:
            maxEle = max(maxEle,ele)
            maxEles.append(maxEle)
        minRight , ind = nums[-1],len(nums) - 1
        ans = 0
        while ind >= 1:
            if maxEles[ind-1] <= minRight:
                ans = len(nums[:ind])
            ind -= 1
            minRight = min(minRight,nums[ind])
       
        return ans