# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root :
            return 0
        self.ans = 0
        def fn(node,pre,q):
            if not node:
                return self.ans
            if pre==targetSum:
                self.ans+=1
            for i in q:
                if pre-i==targetSum:
                    self.ans+=1
            if node.left:
                fn(node.left,pre+node.left.val,q+[pre])
            if node.right:
                fn(node.right,pre+node.right.val,q+[pre])
            return self.ans
        return fn(root,root.val,[])