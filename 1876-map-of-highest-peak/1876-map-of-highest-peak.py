class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        water , row , col = deque() , len(isWater) , len(isWater[0])
        visited = set()
        for r in range(row):
            for c in range(col):
                if isWater[r][c] == 1:
                    isWater[r][c] = 0
                    water.append((r,c,0))
                    visited.add((r,c))
       
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        
        while water:
            r , c , h = water.popleft()
            for x , y in direction:
                ax ,ay = r + x , c + y
                if 0<=ax < row and 0<= ay < col and (ax,ay) not in visited:
                    isWater[ax][ay] = h + 1
                    water.append((ax,ay,h+1))
                    visited.add((ax,ay))
        return isWater
