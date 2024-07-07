# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q , ind = deque([root]),0
        while q:
            temp = []
            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                    temp.append(n.left.val)
                if n.right:
                    q.append(n.right)
                    temp.append(n.right.val)
            ind += 1
            if ind%2!=0 and q:
                n = len(q)
            
                for i in range(n):
                    
                    q[i].val = temp[n - i - 1]
            
        return root
        