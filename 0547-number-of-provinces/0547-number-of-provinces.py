class Solution:
    def findCircleNum(self, c: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in range(len(c[node])):
                if c[node][neighbor]and neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        n = len(c)

        seen = set()
        ans = 0
        
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        
        return ans
        