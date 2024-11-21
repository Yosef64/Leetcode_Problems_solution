class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls = {(x,y) for x,y in walls}
        g = [[0 for col in range(n)] for row in range(m)]
        for x, y in guards:  
            g[x][y] = 2    
        for x, y in walls:
            g[x][y] = 2
        
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for gx, gy in guards:
            for dx, dy in dirs: 
                x, y = gx, gy
                while True:
                    x += dx
                    y += dy
                    if not 0<=x<m or not 0<=y<n or g[x][y] == 2:
                        break
                    g[x][y] = 1
        count = sum(col == 0 for row in g for col in row)
        return count
