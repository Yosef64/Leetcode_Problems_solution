class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = defaultdict(list)
        for eq in equations:
            if eq[1] != '!':
                graph[eq[0]].append(eq[-1])
                graph[eq[-1]].append(eq[0])
        def dfs(node,path,t):
            if node in path or t == node:
                return not t == node
            for child in graph[node]:
                if not dfs(child,path.union({node}),t):
                    return False
            return True
        for eq in equations:
            if eq[1]=='!' and not (dfs(eq[-1],set(),eq[0]) and dfs(eq[0],set(),eq[-1])):
                return False
        return True
                
