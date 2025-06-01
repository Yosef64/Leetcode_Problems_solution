from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.array = SortedList()
    
    def checkOverlap(self,arr1,arr2):
        m_l , m_r = arr1
        sT , eT = arr2
        return (m_l<=sT <m_r or m_l<eT<=m_r) or (sT<=m_l <eT or sT < m_r <=eT)
        

    def book(self, sT: int, eT: int) -> bool:
        l ,r = 0, len(self.array) - 1
        while l <= r:
            mid = (r-l) // 2 + l
            mid_point = self.array[mid]
            if self.checkOverlap(mid_point,[sT,eT]):
                return False
            if mid_point[-1] <= sT:
                l = mid + 1
            else:
                r = mid - 1
        self.array.add([sT,eT])
        return True
            


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)