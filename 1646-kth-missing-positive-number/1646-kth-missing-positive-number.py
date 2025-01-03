class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cur , val = 1,-1
        miss_n ,n = 0, len(arr)
        while miss_n < k:
            l, r = 0, n - 1
            while l < r:
                mid = (r - l) // 2 + l
                if arr[mid] == cur:
                    l = mid
                    break

                if arr[mid] > cur:
                    r = mid - 1
                else:
                    l = mid + 1
            if arr[l] != cur:
                val = cur
                miss_n += 1
            cur += 1
        return val
