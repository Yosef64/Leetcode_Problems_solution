# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def dfs(left,right):
            if left > right:
                return [None]
            ans = []
            for ind in range(left,right+1):
                
                leftTrees = dfs(left,ind-1)
                rightTrees = dfs(ind+1,right)
                for l in leftTrees:
                    for r in rightTrees:
                        node = TreeNode(ind)
                        node.right = r
                        node.left = l
                        ans.append(node)
            return ans
        return dfs(1,n)        