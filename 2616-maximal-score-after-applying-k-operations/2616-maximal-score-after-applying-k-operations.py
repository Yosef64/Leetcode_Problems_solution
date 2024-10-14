class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap , score = [] , 0
        for num in nums:
            heapq.heappush(heap,-num)
        for _ in range(k):
            Max = -heapq.heappop(heap)
            score += Max
            heapq.heappush(heap,-math.ceil(Max/3))
        return score