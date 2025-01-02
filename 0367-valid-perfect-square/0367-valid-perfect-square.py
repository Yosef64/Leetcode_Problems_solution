class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l , r = 1, num//2 + 1
        while l <= r:
            mid = (r - l) // 2 + l
            midSq = mid ** 2
            if midSq == num:return True

            if midSq < num:
                l = mid + 1
            else:
                r = mid - 1
        return False