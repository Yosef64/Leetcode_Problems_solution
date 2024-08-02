# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        if not root:
            return []
        ans = [root.val]
        while q:
            c = deque(q)
            for i in c:
                if i.left:
                    q.append(i.left)
                if i.right:
                    q.append(i.right)
                q.popleft()
            if q:
                ans.append(q[-1].val)
        return ans
            