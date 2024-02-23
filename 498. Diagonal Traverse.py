class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n,m = len(mat),len(mat[0])
        ans = []
        def dec(row,col):
            while row < n and col >= 0:
                ans.append(mat[row][col])
                row,col = row + 1, col - 1
            return (row ,col + 1) if row < n else (row - 1 ,col + 2)
        def inc(row,col):
            while row >=0 and col <m:
                ans.append(mat[row][col])
                row,col = row-1,col+1
            return (row+1,col) if col < m else (row+2,col-1)
        i,j = 0,0
        while i < n and j < m:
            tn,tm = inc(i,j)
            i , j = dec(tn,tm)
        return ans
