class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row , col = len(mat) , len(mat[0])
        q = []
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i,j))
                    continue
                mat[i][j] = '#'
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        for r ,c in q:
            for x , y in direction:
                ax , ay = r + x , c + y
                if 0<= ax<row and 0<=ay < col and mat[ax][ay]=='#':
                    mat[ax][ay] = mat[r][c] + 1
                    q.append((ax,ay))
        return mat
            