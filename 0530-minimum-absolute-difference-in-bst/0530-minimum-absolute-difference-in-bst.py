# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre, res = None, float("inf")
        def dfs(node):
            nonlocal res, pre
            if not node:
                return res
            dfs(node.left)
            res = min(res,abs(pre - node.val)) if pre != None else res
            pre = node.val
            dfs(node.right)
            return res
        return dfs(root)