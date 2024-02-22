class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count , n , m = 0,len(strs),len(strs[0])
        for i in range(m):
            pre = strs[0][i]
            for j in range(1,n):
                
                if strs[j][i] < pre:
                    
                    break
                pre = strs[j][i]
            else:
                
                count += 1
        return m - count
            
        
