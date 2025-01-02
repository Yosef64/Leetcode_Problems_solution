class Solution:
    def arrangeCoins(self, n: int) -> int:
        def calculateSum(mid):
            return (mid)*(1+mid) / 2
        
        l, r = 1, n
        while l <= r:
            mid = (r - l) // 2 + l
            s = calculateSum(mid)
            if s == n:return mid

            if s < n:
                l = mid + 1
            else:
                r = mid - 1
        return r
            
        