class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dic = {
            1:{"t":[],"b":[],'r':[3,5,1],'l':[4,6,1]},
            2:{"t":[3,4,2],"b":[5,6,2],'r':[],'l':[]},
            3:{"t":[],"b":[5,6,2],'r':[],'l':[4,6,1]},
            4:{"t":[],"b":[6,5,2],'r':[3,1,5],'l':[]},
            5:{"t":[3,4,2],"b":[],'r':[],'l':[4,6,1]},
            6:{"t":[3,4,2],"b":[],'r':[3,5,1],'l':[]}
        }
        row , col = len(grid) , len(grid[0])
        def isFit(cur,Next):
            if Next[0] >= row or Next[0] < 0 or Next[1] >= col or Next[1] < 0:
                return False
            curVal , nextVal = grid[cur[0]][cur[1]] ,grid[Next[0]][Next[1]]
            if Next[0]==cur[0] and Next[1] > cur[1]:
                return nextVal in dic[curVal]['r']
            if Next[0]==cur[0] and Next[1] < cur[1]:
                return nextVal in dic[curVal]['l']
            if Next[0] > cur[0] and Next[1] == cur[1]:
                return nextVal in dic[curVal]['b']
            
            return nextVal in dic[curVal]['t']
        # print(isFit([0,1],[0,2]))
        q = deque([(0,0)])
        visited = set()
        while q:
            r , c = q.popleft()
            visited.add((r,c))
            # print(r,c)
            if r == row - 1 and c == col - 1:return True
            direct = [[0,1],[1,0],[0,-1],[-1,0]]
            for x , y in direct:
                if (r+x,c+y) in visited or not isFit([r,c],[r+x,c+y]):
                    # print("not",)
                    continue
                
                q.append((r+x,c+y))
        # print(isFit([0,0],[1,0]))
        return False