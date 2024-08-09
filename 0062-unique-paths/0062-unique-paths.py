class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m-1)]
        grid.append([1 for _ in range(n)])
        
        for row in range(m - 2 , -1 , -1):
            for col in range(n - 1,-1,-1):
                if col < n - 1:
                    grid[row][col] += grid[row][col + 1]
                
                grid[row][col] += grid[row+1][col]
        return grid[0][0]

