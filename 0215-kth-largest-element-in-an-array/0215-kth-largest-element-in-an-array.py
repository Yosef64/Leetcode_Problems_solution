class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*num for num in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -1*heapq.heappop(nums)