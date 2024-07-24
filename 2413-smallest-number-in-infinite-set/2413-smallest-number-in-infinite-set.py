class SmallestInfiniteSet:

    def __init__(self):
        self.Min = 1
        self.s = set()
    def popSmallest(self):
        if self.s:
            r = min(self.s)
            self.s.remove(r)
            return r
        
        self.Min += 1
        return self.Min - 1
    def addBack(self, num):
        if self.Min > num:
            self.s.add(num) 
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)