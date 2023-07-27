class MyCircularDeque:

    def __init__(self, k: int):
        self.list = deque([])
        self.limit = k
        
    def insertFront(self, value: int) -> bool:
        if len(self.list)<self.limit:
            self.list.appendleft(value)
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if len(self.list)<self.limit:
            self.list.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.list) > 0:
            self.list.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.list) >0:
            self.list.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.list)>0:
            return self.list[0]
        return -1
            
    def getRear(self) -> int:
        if len(self.list) >0 :
            return self.list[-1]
        return -1
    def isEmpty(self) -> bool:
        if len(self.list) ==0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.list)==self.limit:
            return True
        return False


