# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def decision(self,n1,n2):
        c1 , c2 = True,True
        if n1.left:
            c1 = c1 and n1.left.val == n2.left.val if n2.left else False
            c2 = c2 and n1.left.val == n2.right.val if n2.right else False
        if n1.right:
            c1 = c1 and n1.right.val == n2.right.val if n2.right else False
            c2 = c2 and n1.right.val == n2.left.val if n2.left else False
        if not n1.left:
            c1 = c1 and n2.left == None
            c2 = c2 and n2.right == None
        if not n1.right:
            c1 = c1 and n2.right == None
            c2 = c2 and n2.left == None
        return c1,c2

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 and root2 and root1.val != root2.val:return False
        def dfs(node1,node2):
            if not node1 or not node2:
                return node1 == node2
            
            con1 ,con2 = self.decision(node1,node2)

            
            if not con1 and  not con2:return False

            return dfs(node1.left,node2.left if con1 else node2.right) and dfs(node1.right,node2.right if con1 else node2.left)
        return dfs(root1,root2)