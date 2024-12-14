"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res =  []
        left , right= 1 , z
        while left <= right:
            st = customfunction.f(left  ,right)
            
            if st == z:
                
                res.append([left,right])
                
                left, right = left+1, right-1
            elif st < z:
                left += 1
            else:
                right -= 1
        left, right = 1, z
        while left < right:
            rv = customfunction.f(right,left)
            if rv == z:
                
                res.append([right,left])
                
                left, right = left+1, right-1
            elif rv < z:
                left += 1
            else:
                right -= 1

        return res
        