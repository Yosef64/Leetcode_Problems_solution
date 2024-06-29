class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        listLand , row , col = [] , len(grid),len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    listLand.append((r,c,0))
        # print(listLand)
        q , visited = deque(listLand) , set()
        if len(listLand) in (0,row*row):return -1
        direction , ans = [[1,0],[0,1],[-1,0],[0,-1]] , -1
        while q:
            r , c , level = q.popleft()
            ans = max(ans,level)
            for x , y in direction:
                ax , ay = x + r, y + c
                if 0 <= ax < row and 0 <= ay < col and (ax,ay) not in visited:
                    q.append((ax,ay,level+1))
                    visited.add((ax,ay))
            
       
        return ans 