class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans = -1
        v = set()
        def dfs(cur,ind,dic):
            nonlocal ans
            if cur in dic:
                ans = max(ans,ind - dic[cur])
                return 
            if edges[cur] == -1 or cur in v:
                return
            
            
            v.add(cur)
            dic[cur] = ind
            return dfs(edges[cur],ind+1,dic)
        for ind in range(len(edges)):
            dfs(ind,0,{})
        return ans
            
