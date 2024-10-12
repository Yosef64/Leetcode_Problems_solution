class Solution:
    def minGroups(self, inter: List[List[int]]) -> int:
        inter.sort()
        heap = []
        for x , y in inter:
            if heap and heap[0][0] < x:
                heapq.heappop(heap)
            heapq.heappush(heap,[y,x]) 
        return len(heap)
