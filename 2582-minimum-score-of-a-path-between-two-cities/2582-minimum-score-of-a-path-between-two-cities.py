class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        root = [i for i in range(n+1)]

        def find(a):
            if root[a] == a:
                return a
            root[a] = find(root[a]) # path compression  
            return root[a]

        def union(a, b):
            a = find(a)
            b = find(b)
            root[a] = b

        for a, b, _ in roads:
            union(a,b)

        return min(d for a,b,d in roads if find(n) == find(a))