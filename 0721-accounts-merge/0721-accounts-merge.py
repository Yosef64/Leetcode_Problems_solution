class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic = defaultdict(list)
        v = set()
        for ind in range(len(accounts)):
            for email in accounts[ind][1:]:
                dic[email].append(ind)
        def dfs(ind):
            if ind in v:return set()

            v.add(ind)
            s = set()
            for word in accounts[ind][1:]:
                for child in dic[word]:
                    s = s.union(dfs(child))
                s.add(word)
            return s
        ans = []
        for ind in range(len(accounts)):
            if ind not in v:
                res = [accounts[ind][0]] + sorted(dfs(ind))
                ans.append(res)
        return ans
