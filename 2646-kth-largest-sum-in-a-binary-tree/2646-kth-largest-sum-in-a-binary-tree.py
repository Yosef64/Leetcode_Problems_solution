# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSums(self,root):
        arr , q = [root.val],deque([root])
        while q:
            levelSum = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    levelSum += node.left.val
                    q.append(node.left)
                if node.right:
                    levelSum += node.right.val
                    q.append(node.right)
            if levelSum:
                arr.append(levelSum)
        return sorted(arr,reverse=True)
            
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        result = self.getSums(root)
        
        return result[k-1] if k <= len(result) else -1