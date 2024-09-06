class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)
        parent = {i: i for i in range(1,size+1)}
        def find(city):
            if city == parent[city]:
                return city
            return find(parent[city])

        def union(x,y):
            root1 = find(x)
            root2 = find(y)
            if root1 != root2:
                parent[root2] = root1

        for fE,sE in edges:
            if find(fE) == find(sE):
                return [fE,sE]
        
            union(fE,sE)

            
        