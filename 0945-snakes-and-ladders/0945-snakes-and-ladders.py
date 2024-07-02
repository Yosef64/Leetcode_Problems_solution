class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        row = len(board) 
        
        def fn(num):
            r = (num - 1) // row 
            c =( num - 1) % row
            if r % 2:
                c = row - 1 - c
            return [row - 1 - r,c]
        
        q = deque([[1,0]])
        visited = set()
        while q:
            num , moves = q.popleft()
            
            for move in range(1,7):
                nMove = num + move
                r , c = fn(nMove)
                print(r,c)
                if board[r][c] != -1:
                    nMove = board[r][c]
                if nMove == row * row:
                    return moves + 1
                if nMove not in visited:
                    visited.add(nMove)
                    q.append([nMove,moves + 1])
        return -1
