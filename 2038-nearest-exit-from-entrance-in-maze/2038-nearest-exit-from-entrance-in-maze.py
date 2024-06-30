class Solution:
    def nearestExit(self, maze: List[List[str]], en: List[int]) -> int:
        q , visited = deque([(en[0],en[1],0)]) , set()
        # print(q)
        row , col = len(maze) , len(maze[0])
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        ans = float("inf")
        while q:
            r , c , l = q.popleft()
            if [r,c]!=en and (r in (0,row-1) or c in (0,col-1)):
                ans = min(ans,l)
            for x,y in direction:
                ax , ay = r + x,c + y
                if  0<=ax<row and 0<=ay<col and (ax,ay) not in visited and maze[ax][ay] != '+':
                    q.append((ax,ay,l+1))
                    visited.add((ax,ay))
        return ans if ans!= float("inf") else -1

        