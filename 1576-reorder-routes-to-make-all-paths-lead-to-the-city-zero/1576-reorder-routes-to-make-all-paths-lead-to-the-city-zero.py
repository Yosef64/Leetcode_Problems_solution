class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, node, parent, adj):
        if node not in adj:
            return
        for nei in adj[node]:
            neighbor = nei[0]
            sign = nei[1]
            if neighbor != parent:
                self.count += sign
                self.dfs(neighbor, node, adj)

    def minReorder(self, n, connections):
        adj = defaultdict(list)
        for connection in connections:
            adj[connection[0]].append([connection[1], 1])
            adj[connection[1]].append([connection[0], 0])

        self.dfs(0, -1, adj)
        return self.count
