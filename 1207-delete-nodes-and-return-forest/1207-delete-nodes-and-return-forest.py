# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        parent , nodeDelete = defaultdict(TreeNode) , set([*to_delete,None])
        ans = []
        def dfs(node):
            nonlocal ans , parent
            if node.left:
                parent[node.left.val] = node.val
                node.left = dfs(node.left)
            if node.right:
                parent[node.right.val] = node.val
                node.right = dfs(node.right)
            
            if parent[node.val] in nodeDelete and node.val not in nodeDelete:
                ans.append(node)
            if node.val in nodeDelete:return None
            return node
        dfs(root)
        if root.val not in nodeDelete:
            ans.append(root)
        return  ans