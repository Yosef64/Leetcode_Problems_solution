class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ch = set(banned)
        ans, pre = 0,0
        ind = 1
        while ind <= n and pre+ind <= maxSum:
            if ind not in ch:
                ans += 1
                pre += ind
            ind += 1
        
            
        return ans
                
        
                     
        