class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for fr,to in edges:
            graph[to].append(fr)
       
        ans = [[] for _ in range(n)]
        def dfs(cur):
            nonlocal ans
            if ans[cur]:
                return ans[cur]
            
            temp = graph[cur][:]
            for child in graph[cur]:
                temp.extend(dfs(child))
            
            ans[cur] = list(sorted(set(temp)))
            return ans[cur]
        for ind in range(n):
            if ans[ind]:
                continue
            
            dfs(ind)
        return ans
        