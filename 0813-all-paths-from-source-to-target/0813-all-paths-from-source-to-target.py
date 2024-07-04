class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dic , n = {} , len(graph)
        for ind in range(len(graph)):
            dic[ind] = graph[ind]
        
        visited = set()
        q , ans = deque([[0]]) , []
        while q:
            ls = q.popleft()
            
            for ele in dic[ls[-1]]:
                # if ele in visited:
                #     continue
                cur = ls + [ele]
                
                if ele == n - 1:
                    ans.append(cur)
                else:q.append(cur)
                
            # print(q)
                
        return ans