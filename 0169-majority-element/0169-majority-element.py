class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count , n = defaultdict(int), len(nums)
        for num in nums:
            count[num] += 1
            if count[num] >= n/2:
                return num
            
        