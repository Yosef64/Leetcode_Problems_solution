class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if not edges:return 0 if n == 1 else -1
        v, graph = set(),defaultdict(list)
        edge = {ind:True for ind in range(n)}
        for g,s in edges:
            graph[g].append(s)
        def dfs(node):
            if node in v:
                return
            v.add(node)
            for child in graph[node]:
                
                dfs(child)
            return
        for g,s in edges:
            
            dfs(s)
        # print(edge,graph)
        res = None
        for key in range(n):
            if key not in v:
                if res != None:return -1

                res = key
        return res

