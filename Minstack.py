class MinStack:

    def __init__(self):
        self.stack = []
        self.pref_min = [float("inf")]
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.pref_min.append(min(self.pref_min[-1],val))
    def pop(self) -> None:
        self.stack.pop()
        self.pref_min.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pref_min[-1]