class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [x for x in range(1,n+1)]
        i = 0
        while len(arr) > 1:
            next_ = (i+k-1)%len(arr)
            
            arr.remove(arr[next_])
            i = next_
        return arr[0]
            
            
