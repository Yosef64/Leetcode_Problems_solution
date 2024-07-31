class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph) 
        safe , v = [True]*n , set()
        def dfs(cur,curV):
            if cur in curV:
                return False
            if cur in v:
                return safe[cur]
            v.add(cur)
            for child in graph[cur]:
                safe[cur] = safe[cur] and dfs(child,curV.union(set([cur])))
            
            return safe[cur]
        for ind in range(n):
            if ind not in v:
                dfs(ind,set())
        
        return [ind for ind in range(n) if safe[ind]]
