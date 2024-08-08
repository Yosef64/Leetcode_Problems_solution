# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def getNodes(ls):
            if len(ls) == 1:
                return ls[0]
            return [ls[0][0],ls[1][1]]
        unOrdered = []
        lastNode = None
        def dfs(node):
            nonlocal lastNode
            if not node:return

            dfs(node.left)

            if lastNode and node.val < lastNode.val:
                unOrdered.append([lastNode,node])
            
            lastNode = node
            dfs(node.right)

        
        dfs(root)
        node1,node2 = getNodes(unOrdered)
        node1.val , node2.val = node2.val , node1.val
        
        
        