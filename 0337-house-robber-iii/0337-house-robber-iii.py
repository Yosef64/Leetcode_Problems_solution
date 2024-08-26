# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node,per):
            if not node:
                return 0
            
            include = 0
            if per:
                include = node.val + dp(node.left,False)+dp(node.right,False)
            
            exclude = dp(node.left,True) + dp(node.right,True)
            return max(include,exclude)
        return dp(root,True)
        