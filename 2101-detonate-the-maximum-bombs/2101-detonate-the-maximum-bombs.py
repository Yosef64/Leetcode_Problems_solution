import math
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        v = set()
        ans = 0
        def fn(ls,i):
            x1 , y1 , r1 = ls
            count = 1
            v.add(i)
            for ind in range(len(bombs)):
                if ind in v:continue
                x2,y2,r2 = bombs[ind]
                distance = sqrt((x2-x1)**2 + (y2-y1)**2)
                if distance <= r1:
                    count += fn([x2,y2,r2],ind)    
            return count
        for ind in range(len(bombs)):
            ans = max(ans,fn(bombs[ind],ind))
            v = set()
        return ans
                
               