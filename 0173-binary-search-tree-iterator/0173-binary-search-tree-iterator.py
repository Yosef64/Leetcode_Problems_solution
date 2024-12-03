# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = self.InOrder(root)

    def next(self) -> int:
        return self.res.popleft()
        

    def hasNext(self) -> bool:
        return len(self.res) != 0
        
    def InOrder(self,root) -> List[int]:
        res = deque([])
        def fn(node):
            nonlocal res
            if not node:return None
            fn(node.left)
            res.append(node.val)
            fn(node.right)
            return
        fn(root)
        return res

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()