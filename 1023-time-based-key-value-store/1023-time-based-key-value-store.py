class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        
        values = self.dic[key]
        if not values:return ""
        l, r = 0 , len(values) - 1
        
        while l < r:
            mid= (r - l) // 2 + l
            val , t =values[mid]
            
            if t <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if values[l][1] <= timestamp:
            return values[l][0]
        if l - 1 >=0 and values[l-1][1] <= timestamp:
            return values[l-1][0] 
        return ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)