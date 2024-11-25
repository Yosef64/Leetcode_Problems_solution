class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols = len(board),len(board[0])
        regions = [(row,col) for row in range(rows) for col in range(cols) if board[row][col] == "O"]
        print(regions)
        v,tv = set(),set()
        def dfs(row,col):
            if not 0<=row<rows or not 0<=col<cols or board[row][col]=="X" or (row,col) in tv:
                return not 0<=row<rows or not 0<=col<cols
            tv.add((row,col))
            v.add((row,col))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            con = False
            for x,y in directions:
                con = con or dfs(row+x,col+y)
            return con
        for row,col in regions:
            if (row,col) not in v and not dfs(row,col):
                # print(tv)
                for r,c in tv:
                    board[r][c] = "X"
            tv = set()


        
        