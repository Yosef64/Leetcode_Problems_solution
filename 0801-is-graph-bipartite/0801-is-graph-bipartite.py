class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0] * len(graph)
        def fn(i):
            if odd[i]:
                return True
            
            q = deque([i])
            odd[i] = -1
            while q:
                i = q.popleft()
                for nei in graph[i]:
                    if odd[nei] == odd[i]:
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei] = -1 * odd[i]
            return True
        for i in range(len(graph)):
            if not fn(i):
                return False
        return True