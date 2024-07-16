class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        routes = {(a,b) for a,b in connections}
        dic = defaultdict(list)
        changes , visited = 0 , set([0])
        for a,b in connections:
            dic[a].append(b)
            dic[b].append(a)
        def fn(route):
            nonlocal changes
            for neigbor in dic[route]:
                if neigbor in visited:
                    continue
                if (neigbor,route) not in routes:
                    changes += 1
                
                visited.add(neigbor)
                fn(neigbor)
            return 
        fn(0)
        return changes