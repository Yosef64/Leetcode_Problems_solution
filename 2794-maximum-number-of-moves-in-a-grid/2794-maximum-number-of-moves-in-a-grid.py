class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        @cache
        def dp(row,col):
            moves = 0
            if row - 1 >= 0 and col + 1 < m and grid[row-1][col+1] > grid[row][col]:
                moves = max(moves,1+dp(row-1,col+1))
            if row + 1 < n and col + 1 < m and grid[row+1][col+1] > grid[row][col]:
                print(row,col)
                moves = max(moves,1+dp(row+1,col+1))
            if col + 1 < m and grid[row][col+1] > grid[row][col]:
                moves = max(moves,1+dp(row,col+1)) 
            return moves
        ans = 0
        for ind in range(n):
            ans = max(ans,dp(ind,0))
        
        return ans
        