# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        dic = defaultdict(TreeNode)
        
        q , depth = deque([root]) , deque([root])
        while q:
            temp = deque()
            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                    dic[n.left.val] = n
                    temp.append(n.left)
                if n.right:
                    q.append(n.right)
                    dic[n.right.val] = n
                    temp.append(n.right)
            if q:
                depth = temp
        print(len(depth))  
        visited = set()
        while len(depth) != 1:
            for _ in range(len(depth)):
                n = depth.popleft()
                if dic[n.val] not in visited:
                    visited.add(dic[n.val])
                    depth.append(dic[n.val])

        return depth[0]