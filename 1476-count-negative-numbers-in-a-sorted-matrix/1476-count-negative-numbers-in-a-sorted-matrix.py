class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res ,cols= 0, len(grid[0])
        for row in grid:
            l ,r = 0 , cols - 1
            while l < r:
                mid = (r - l) // 2 + l

                if row[mid] >= 0:
                    l = mid + 1
                else:
                    r = mid
            if row[r] < 0:
                res += (cols - r)
        return res
            