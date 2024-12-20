# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        Tree , q =[[root]] , deque([root])
        while q:
         
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if len(q) != 0:
                Tree.append(list(q))
        
        for i in range(1,len(Tree),2):
            l ,r = 0, len(Tree[i]) - 1
            while l < r:
                Tree[i][l].val,Tree[i][r].val = Tree[i][r].val,Tree[i][l].val
                l , r = l + 1, r - 1
        return root
