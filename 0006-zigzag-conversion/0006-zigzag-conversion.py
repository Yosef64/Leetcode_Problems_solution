class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:return s
        ans = [""]*numRows
        # print(ans)
        c , p = True,0
        for i,j in enumerate(s):
            ans[p]+=j
            
                
            
            if c:
                p+=1
                if p==numRows-1:c = False
            else:
                p-=1
                if p==0:c = True
        return "".join(ans)
                
        