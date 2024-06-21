# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        def fn(parent,node):
            fra = parent % 2 
            
            if node.left:
                self.ans = self.ans + node.left.val if fra == 0 else self.ans + 0
                fn(node.val,node.left)
            if node.right:
                self.ans = self.ans + node.right.val if fra == 0 else self.ans + 0
                fn(node.val,node.right)
            return self.ans
        return fn(-1,root)