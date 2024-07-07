# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):

        self.root = root
        self.root.val = 0
        def fn(node):
            if node.left:
                node.left.val = 2*node.val + 1
                fn(node.left)
            if node.right:
                node.right.val = 2*node.val + 2
                fn(node.right)
            return
        fn(self.root)
        

    def find(self, target: int) -> bool:
        def dfs(node):

            if node and node.val == target:
                return True
            if not node or node.val > target:
                return False

            
            return dfs(node.left) or dfs(node.right)
        return dfs(self.root)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)