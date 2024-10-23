# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLevelSum(self,root):
        res , q = [],deque([root])
        while q:
            levelsum = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    levelsum += node.left.val
                    q.append(node.left)
                if node.right:
                    levelsum += node.right.val
                    q.append(node.right)
            if levelsum:
                res.append(levelsum)
        return res
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q , level = deque([root]) , 0
        sums = self.getLevelSum(root)
        root.val = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                childsum = 0
                if node.left:
                    childsum += node.left.val
                    q.append(node.left)
                if node.right:
                    childsum += node.right.val
                    q.append(node.right)
                
                if node.left:
                    node.left.val = sums[level] - childsum
                if node.right:
                    node.right.val = sums[level] - childsum
            level += 1
        return root