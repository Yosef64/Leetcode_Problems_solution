class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows , cols = len(board),len(board[0])
        matrix = [[ele for ele in row] for row in board]
        def GetLive(row,col):
            count = 0
            direction = [[1,1],[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[1,-1],[-1,1]]
            for x,y in direction:
                tr,tc = row+x,col+y
                
                if 0<= tr <rows and 0<=tc<cols:
                    count += board[tr][tc]
           
            return count
        for row in range(rows):
            for col in range(cols):
                lives = GetLive(row,col)
                # print((row,col),lives)
                if board[row][col]:
                    matrix[row][col] = 0 if lives < 2 or lives > 3 else matrix[row][col]
                else:
                    matrix[row][col] = 1 if lives == 3 else matrix[row][col]
        for row in range(rows):
            for col in range(cols):
                board[row][col] = matrix[row][col]



        