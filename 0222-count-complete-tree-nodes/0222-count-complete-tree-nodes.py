# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return count
            count += 1
            dfs(node.left)
            dfs(node.right)
            return count
        return dfs(root)
        