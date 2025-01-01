class SnapshotArray:

    def __init__(self, length: int):
        self.dic = defaultdict(list)
        self.snaps = 0

    def set(self, index: int, val: int) -> None:
        self.dic[index].append([val,self.snaps])
        

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1
        
    def get(self, index: int, snap_id: int) -> int:
        values = self.dic[index]
        if not values:return 0
        l, r = 0 , len(values)- 1
        while l < r:
            mid = (r - l) // 2 + l
            val,snap = values[mid]
            if snap > snap_id:
                r = mid - 1
            else:
                l = mid + 1
        
        if values[l][1] <= snap_id:
            return values[l][0]
        if l - 1 >=0 and values[l - 1][1] <= snap_id:
            return values[l - 1][0]
        return 0 


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)