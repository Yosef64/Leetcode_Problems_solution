class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)
        parent = {i: i for i in range(1,size+1)}

        def union(x,y):
            parentX = parent[x]
            parentY = parent[y]

            for node in parent:
                if parent[node] == parentX:
                    parent[node] = parentY

        for fE,sE in edges:
            if parent[fE] == parent[sE]:
                return [fE,sE]
            union(fE,sE)

            
        