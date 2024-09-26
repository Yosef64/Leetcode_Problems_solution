from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.books = SortedList()
    def overlap_(self,interval1, interval2):  
        # print(interval1,interval2)
        start1, end1 = min(interval1,interval2)  
        start2, end2 = max(interval1,interval2)
        
        return end1 > start2

    def book(self, start: int, end: int) -> bool:
        l , r = 0,len(self.books)-1
        while l <= r:
            mid = (r-l)//2 + l
            left , right = self.books[mid]

            if self.overlap_((start,end),(left,right)):
                return False
            
            if right > start:
                r = mid - 1
            else:
                l = mid + 1
        self.books.add([start,end])
        return True



        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)