class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows ,  cols = len(grid) , len(grid[0])
        for i in range(cols - 2,-1,-1):
            grid[-1][i] += grid[-1][i+1]
        for row in range(rows - 2, -1, -1):
            for col in range(cols -1 , -1,-1):
                if col < cols - 1:
                    preC , preR= grid[row][col + 1],grid[row+1][col]
                    grid[row][col] = min(grid[row][col] + preC,grid[row][col]+preR)
                    continue
                grid[row][col]+= grid[row+1][col]
                
                
        return grid[0][0]

