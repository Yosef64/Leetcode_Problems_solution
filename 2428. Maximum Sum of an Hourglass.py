class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxAns = sum(grid[0][:3])+grid[1][1] + sum(grid[2][:3])
        n , m = len(grid),len(grid[0])
        for i in range(0,n-2):
            left , right = 0,3
            f ,s = sum(grid[i][:3]),sum(grid[i+2][:3])
            total = f+s+grid[i+1][1]
            maxAns = max(total,maxAns)
            while right < m:
                f,s = f - grid[i][left] ,s-grid[i+2][left]
                f,s = f+grid[i][right],s+grid[i+2][right]
                left , right = left + 1,right+1
                total = f + s + grid[i+1][left+1]
                maxAns = max(maxAns,total)
        return maxAns
