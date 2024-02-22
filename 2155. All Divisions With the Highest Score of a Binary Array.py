class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        zero,one = 0,count[1]
        ans = defaultdict(list)
        maxE = zero+one
        ans[maxE].append(0)
        for ind in range(len(nums)):
            if nums[ind] == 0:
                zero += 1
            else:
                one -= 1
            d = zero + one
            if maxE <= d:
                maxE = d
                ans[maxE].append(ind+1)
        return ans[maxE]
        
