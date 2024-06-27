# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        dic = {}
        def dfs(node):
            
            if node.left:
                dic[node.left.val] = node
                dfs(node.left)
            if node.right:
                dic[node.right.val] = node
                dfs(node.right)
            if node.val == target.val:
                
                dic["start"] = node
            return 
        dfs(root)
        # print(dic["start"])
        start , level = dic["start"] ,0
        visited , q = set() , deque([start])
        ans = []
        while q and level < k:
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node.val)
                if node.left and node.left.val not in visited:
                    q.append(node.left)
                if node.right and node.right.val not in visited:
                    q.append(node.right)
                if node.val in dic and dic[node.val].val not in visited:q.append(dic[node.val])
            level += 1
            
            
        for node in q:
            ans.append(node.val)
        return ans