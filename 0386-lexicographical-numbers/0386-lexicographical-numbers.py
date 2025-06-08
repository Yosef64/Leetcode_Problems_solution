class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(num):
            nonlocal ans
            intNum = int(num)
            if intNum > n:
                return 
            ans.append(intNum)
            for inx in range(10):
                dfs(num+str(inx))
                    
        for inx in range(1,10):
            dfs(str(inx))
        return ans

        