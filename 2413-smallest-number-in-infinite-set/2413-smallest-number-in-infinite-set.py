class SmallestInfiniteSet:

    def __init__(self):
        self.Min = 1
        self. heap= []
    def popSmallest(self):
        if self.heap:
            r = heapq.heappop(self.heap)
            while self.heap and self.heap[0] == r:
                heapq.heappop(self.heap)
            return r
        
        self.Min += 1
        return self.Min - 1
    def addBack(self, num):
        if self.Min > num:
            heapq.heappush(self.heap,num)
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)