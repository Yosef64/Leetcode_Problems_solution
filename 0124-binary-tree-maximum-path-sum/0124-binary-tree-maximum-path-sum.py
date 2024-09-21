# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-infinity")
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            lPath,rPath , both = node.val + left ,node.val+right,node.val+left+right
            Max = max(lPath,rPath,node.val)
            ans = max(ans,Max,both)
            return Max
        dfs(root)
        return ans