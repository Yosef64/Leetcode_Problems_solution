class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def fn(ans,ind):
            if ind==n:
                return ans
            pre = ans[:]
            ans=ans.replace('1','2')
            ans=ans.replace('0','1')
            ans = ans.replace('2','0')
            rte = ans[::-1]
            return fn(pre+'1'+ rte,ind+1)
        final = fn('0',1)
        
        return final[k-1]
            