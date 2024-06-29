class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        blue , red = defaultdict(list),defaultdict(list)
        for edge1,edge2 in redEdges:
            red[edge1].append(edge2)
        for edge1,edge2 in blueEdges:
            blue[edge1].append(edge2)
        ans = [-1] * n
        ans[0] = 0
        def fn(isRed):
            q , level = deque([[0,isRed]]), 1
            visited = set()
            while q:
                for _ in range(len(q)):
                    edge , isRed = q.popleft()
                    ls = red[edge] if isRed else blue[edge]
                    visited.add((edge,isRed))
                    for child in ls:
                        if (child,not isRed) in visited:continue
                        ans[child] = level if ans[child] == -1 else min(ans[child],level)
                        q.append([child,not isRed])
                level += 1
        fn(True)
        fn(False)
        return ans