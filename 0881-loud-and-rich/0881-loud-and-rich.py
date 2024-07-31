class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        ans = [ind for ind in range(n)]
        graph = defaultdict(list)
        for a , b in richer:
            graph[b].append(a)
        v = set()
        def dfs(cur):
            nonlocal ans
            if cur in v:
                return ans[cur]
            v.add(cur)
            for child in graph[cur]:
                Min = dfs(child)
                if quiet[Min] < quiet[ans[cur]]:
                    ans[cur] = Min
            return ans[cur]

        for ind in range(n):
            dfs(ind)

        return ans

        