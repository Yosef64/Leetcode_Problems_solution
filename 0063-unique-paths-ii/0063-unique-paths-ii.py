class Solution:
    def uniquePathsWithObstacles(self, obGrid: List[List[int]]) -> int:
        if obGrid[-1][-1] or obGrid[0][0]:return 0
        rows , cols = len(obGrid),len(obGrid[0])
        grid = [[0]*cols for _ in range(rows)]
        grid[-1][-1] = 1
        for col in range(cols-2,-1,-1):
            if obGrid[-1][col] != 1:
                grid[-1][col] = grid[-1][col+1]
        for row in range(rows-2,-1,-1):
            for col in range(cols-1,-1,-1):
                if not obGrid[row][col]:
                    grid[row][col] = grid[row+1][col] + grid[row][col+1] if col < cols-1 else grid[row+1][col]
        return grid[0][0]

       