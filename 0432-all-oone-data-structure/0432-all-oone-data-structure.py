class Node:
    def __init__(self,val=0,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next

class AllOne:

    def __init__(self):
        self.count , self.pair = {} , {}
        self.start = Node()
        self.end = self.start
       
    def inc(self, key: str) -> None:
        if key in self.count:
            self.count[key] += 1
            cur = self.pair[key]
            prev , next = cur.prev , cur.next
            if not next and prev.val and self.count[prev.val] < self.count[key]:
                self.end = prev
            while prev.val and self.count[prev.val] < self.count[cur.val]:
                prev.next = next
                if next:
                    next.prev = prev
                    next = next.prev
                else:
                    next = prev
                prev = prev.prev
            cur.prev,cur.next = prev,next
            prev.next = cur
            if next:
                next.prev = cur
        else:
            self.count[key] , newNode = 1 , Node(key)
            self.pair[key] , self.end.next = newNode , newNode
            newNode.prev , self.end = self.end , self.end.next
        # print(self.end.val)
    def dec(self, key: str) -> None:
        # print("dec",self.end.val)
        self.count[key] -= 1
        cur = self.pair[key]
        prev , next = cur.prev , cur.next
        while next and self.count[next.val] > self.count[cur.val]:
            prev.next = next
            next.prev = prev
            next = next.next
            prev = prev.next
        cur.prev , cur.next = prev,next
        if not next:
        
            if not self.count[key]:
                self.end = prev
                prev.next = None
                del self.count[key]
                del self.pair[key]
            else:
                prev.next = cur
        else:
            if prev:
                prev.next = cur 
            next.prev = cur
    def getMaxKey(self) -> str:
        return self.start.next.val if self.start.next else ""
        
    def getMinKey(self) -> str:
        # print(self.count)
        return self.end.val if self.end.val else ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()