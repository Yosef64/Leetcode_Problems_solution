class MapSum:

    def __init__(self):
        self.hash = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.hash[key] = val

    def sum(self, prefix: str) -> int:
        pre = 0
        for key in self.hash:
            if key[:len(prefix)] == prefix:
                pre += self.hash[key]
        return pre


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)